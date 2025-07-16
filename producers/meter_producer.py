import time
from interfaces.i_producer import IProducer
from services.simulator import MeterSimulatorService

from services.app_logger import get_logger

logger = get_logger(__name__)


class MeterProducer(IProducer):
    def __init__(self, broker):
        self.broker = broker
        self.simulator = MeterSimulatorService()

    def produce(self):
        while True:
            message = {
                'timestamp': time.time(),
                'meter': self.simulator.simulate()
            }
            self.broker.publish(message)
            logger.debug(f'Meter Sent: {message}')
            time.sleep(2)
