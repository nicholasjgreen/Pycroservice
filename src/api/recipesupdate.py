from src.Adapters import RabbitmqAdapter
from src.Services import RecipeUpdateService
import uuid

def create_recipe(recipe):
    print("Creating new recipe")
    if recipe["id"] == "":
        recipe["id"] = str(uuid.uuid1())
    print(recipe["id"])
    conn = RabbitmqAdapter.get_connection()
    chan = RabbitmqAdapter.get_channel(conn)
    RecipeUpdateService.send_to_queue(chan, recipe)

def update_recipe(recipe):
    print("Updating recipe")
    conn = RabbitmqAdapter.get_connection()
    chan = RabbitmqAdapter.get_channel(conn)
    RecipeUpdateService.send_to_queue(chan, recipe)
