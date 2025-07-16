import pika
import json
from interfaces.i_broker import IBroker
from pika.exceptions import AMQPConnectionError, UnroutableError

from services.app_logger import get_logger
from utils.retry_exceptions import retry

logger = get_logger(__name__)


class RabbitMQClient(IBroker):
    """
    RabbitMQ client for publishing and consuming messages.
    """

    @retry(max_retries=10, delay=3, exception_types=(AMQPConnectionError, UnroutableError,))
    def __init__(self, host='rabbitmq', queue='meter_queue'):
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
        logger.debug('RabbitMQ Connected successfully.')

    @retry(max_retries=5, delay=2, exception_types=(AMQPConnectionError, UnroutableError,))
    def publish(self, message: dict):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=json.dumps(message).encode('utf-8'))
        logger.debug(f'Published message to {self.queue}: {message}')

    @retry(max_retries=5, delay=2, exception_types=(AMQPConnectionError, UnroutableError,))
    def consume(self, callback):
        def wrapped_callback(ch, method, properties, body):  # noqa: F841
            logger.debug(f'Received message from {self.queue}: {body}')
            callback(json.loads(body))

        self.channel.basic_consume(queue=self.queue, on_message_callback=wrapped_callback, auto_ack=True)
        self.channel.start_consuming()
        logger.debug('Started consuming messages from RabbitMQ.')
