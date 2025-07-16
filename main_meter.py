from producers.meter_producer import MeterProducer
from broker.rabbitmq_client import RabbitMQClient


def main():
    broker = RabbitMQClient()
    meter_producer = MeterProducer(broker)
    meter_producer.produce()


if __name__ == '__main__':
    main()
