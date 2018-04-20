from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os


def get_cassandra_cluster():
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster([os.getenv('cass_hostname', 'localhost')], auth_provider=auth_provider)
    return cluster


def get_cassandra_session():
    session = get_cassandra_cluster().connect()
    session.execute("USE Pycro")
    return session


def get_recipes(session):
    return session.execute("SELECT id, name FROM recipes")


def insert_recipe(session, recipe_id, name):
    session.execute(
        """
        INSERT INTO recipes (id, name)
        VALUES (%s, %s)
        """,
        (recipe_id, name))
