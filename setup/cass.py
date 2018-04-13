import uuid
import glob
import json

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def init():
    print("Connecting to local cassandra...")
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(auth_provider=auth_provider)
    session = cluster.connect()
    print("Creating schemas")
    create_keyspace(session)
    session.execute("USE Pycro")
    create_tables(session)
    print("Creating data")
    add_recipes(session)


def create_keyspace(session):
    print("Creating default keyspace")
    session.execute("""CREATE KEYSPACE IF NOT EXISTS Pycro WITH REPLICATION = {
    'class' : 'SimpleStrategy',
    'replication_factor' : 1
    };""")


def create_tables(session):
    print("Creating tables")
    session.execute("""CREATE TABLE IF NOT EXISTS recipes(
        id UUID PRIMARY KEY,
        name text
    );""")


def add_recipes(session):
    print("Adding recipes")
    for filename in glob.glob('./setup/testdata/recipes/*.json'):
        recipe = json.load(open(filename))
        print(recipe['name'])
        add_single_recipe(session, uuid.UUID(recipe["id"]), recipe["name"])


def add_single_recipe(session, id, name):
    session.execute(
        """
        INSERT INTO recipes (id, name)
        VALUES (%s, %s)
        """,
        (id, name)
    )


if __name__ == "__main__":
    init()
