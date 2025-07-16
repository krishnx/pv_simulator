from producers.meter_producer import MeterProducer
from broker.rabbitmq_client import RabbitMQClient
from services.app_logger import get_logger

logger = get_logger(__name__)


def main():
    broker = RabbitMQClient()
    meter_producer = MeterProducer(broker)
    meter_producer.produce()
    logger.debug('Meter Producer started successfully.')


if __name__ == '__main__':
    main()
