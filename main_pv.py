from producers.pv_simulator import PVSimulator
from broker.rabbitmq_client import RabbitMQClient
from services.file_logger import FileLogger

from services.app_logger import get_logger

logger = get_logger(__name__)

def main():
    broker = RabbitMQClient()
    file_logger = FileLogger()
    pv_simulator = PVSimulator(broker, file_logger)
    pv_simulator.produce()
    logger.debug('PV Simulator started successfully.')


if __name__ == '__main__':
    main()
