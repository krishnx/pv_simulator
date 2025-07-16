from producers.pv_simulator import PVSimulator
from broker.rabbitmq_client import RabbitMQClient
from services.logger import FileLogger


def main():
    broker = RabbitMQClient()
    logger = FileLogger()
    pv_simulator = PVSimulator(broker, logger)
    pv_simulator.produce()


if __name__ == '__main__':
    main()
