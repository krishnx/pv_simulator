from datetime import datetime

from interfaces.i_producer import IProducer
from services.simulator import PVSimulatorService
from services.app_logger import get_logger

logger = get_logger(__name__)

class PVSimulator(IProducer):
    def __init__(self, broker, file_logger):
        self.broker = broker
        self.file_logger = file_logger
        self.simulator = PVSimulatorService()

    def produce(self):
        def callback(message):
            meter = message['meter']
            pv = self.simulator.simulate()
            net = round(pv - meter, 2)
            direction = 'Export' if net > 0 else 'Import'
            log_entry = {
                'timestamp': datetime.fromtimestamp(message['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                'meter': meter,
                'pv': pv,
                'net': net,
                'direction': direction,
            }
            self.file_logger.log(log_entry)
            logger.debug(f'PV Logged: {log_entry}')

        self.broker.consume(callback)
