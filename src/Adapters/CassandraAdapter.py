from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def get_cassandra_session():
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(auth_provider=auth_provider)
    session = cluster.connect()
    session.execute("USE Pycro")
    return session


def get_recipes(session):
    return session.execute("SELECT id, name FROM recipes")


def insert_recipe(session, id, name):
    session.execute(
        """
        INSERT INTO recipes (id, name)
        VALUES (%s, %s)
        """,
        (id, name))
