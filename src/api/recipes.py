import Adapters.CassandraAdapter


def get_recipes():
    session = Adapters.CassandraAdapter.get_cassandra_session()
    rows = Adapters.CassandraAdapter.get_recipes(session)
    recipes = []
    for row in rows:
        recipes.append({"id": row.id, "name": row.name})
    return recipes
    #return [
    #    {"id": "1",
    #     "name": "Chilli"},
    #    {"id": "2",
    #     "name": "Chicken in mushroom sauce"}
    #];