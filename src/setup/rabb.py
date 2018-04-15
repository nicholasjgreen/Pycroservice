import src.Services.RecipeUpdateService


def init():
    print("Connecting to RabbitMQ")
    conn = src.Adapters.RabbitmqAdapter.get_connection()
    channel = src.Adapters.RabbitmqAdapter.get_channel(conn)
    print("Creating queues")
    channel.queue_declare(queue=src.Services.RecipeUpdateService.DEFAULT_QUEUE)


if __name__ == "__main__":
    init()
