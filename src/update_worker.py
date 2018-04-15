from src.Adapters import RabbitmqAdapter
from src.Services import RecipeUpdateService
from src.Adapters import CassandraAdapter

print("Connecting to RabbitMQ")
conn = RabbitmqAdapter.get_connection()
channel = RabbitmqAdapter.get_channel(conn)

print("Creating queues")
channel.queue_declare(queue=RecipeUpdateService.DEFAULT_QUEUE)

print("Connecting to Cassandra")
session = CassandraAdapter.get_cassandra_session()

# Start listening
print("Listening to queue...")
RecipeUpdateService.listen_to_queue(channel, session)

print("All done!")