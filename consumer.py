import pika
import time
import logging
import os

logging.basicConfig(level=logging.INFO, filename='demo.log')
username = 'user'
password = os.getenv('rabbitmq-password')

class Consumer:

    def __init__(self):
        self._init_rabbit_consumer()

    def _init_rabbit_consumer(self):
        credentials = pika.PlainCredentials(username, password)
        parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='users')
        def callback(ch, method, properties, body):
            logging.info(f" [x] Received {str(body)}")
        self.channel.basic_consume(queue='users', on_message_callback=callback, auto_ack=True)
        logging.info(' [*] Waiting for messages.')
        self.channel.start_consuming()

if __name__ == "__main__":

    consumer = Consumer()

    while True:
        consumer.consume_from_rabbit()
        time.sleep(5)
