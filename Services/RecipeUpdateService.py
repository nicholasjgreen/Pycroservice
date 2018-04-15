import json
from Adapters import CassandraAdapter
import uuid
DEFAULT_QUEUE = "RecipeUpdates"

CASS_SESSION = None


def listen_to_queue(channel, cass_session):
    print("Listening to queue {}".format(DEFAULT_QUEUE))
    global CASS_SESSION
    CASS_SESSION = cass_session
    channel.basic_consume(process_incoming, queue=DEFAULT_QUEUE, no_ack=False)
    channel.start_consuming()       # This is blocking, forever!


def send_to_queue(channel, message):
    channel.basic_publish(exchange='', routing_key=DEFAULT_QUEUE, body=json.dumps(message))


def process_incoming(ch, method, properties, body):
    print(" [x] Received %r" % body)

    # Parse the JSON
    recipe = json.loads(body)
    CassandraAdapter.insert_recipe(CASS_SESSION, uuid.UUID(recipe["id"]), recipe["name"])

    # Remove from the queue
    ch.basic_ack(delivery_tag=method.delivery_tag)
