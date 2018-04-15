import Services.RecipeUpdateService


def init():
    print("Connecting to RabbitMQ")
    conn = Adapters.RabbitmqAdapter.get_connection()
    channel = Adapters.RabbitmqAdapter.get_channel(conn)
    print("Creating queues")
    channel.queue_declare(queue=Services.RecipeUpdateService.DEFAULT_QUEUE)


if __name__ == "__main__":
    init()
