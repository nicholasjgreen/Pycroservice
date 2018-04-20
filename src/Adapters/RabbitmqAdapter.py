import pika
import os


def get_connection():
    credentials = pika.PlainCredentials("user", "bitnami")
    conn = pika.BlockingConnection(pika.ConnectionParameters(os.getenv("rabb_hostname", "localhost"), 5672, "/", credentials))
    return conn


def get_channel(connection):
    return connection.channel()

