from datetime import datetime

from interfaces.i_producer import IProducer
from services.simulator import PVSimulatorService


class PVSimulator(IProducer):
    def __init__(self, broker, logger):
        self.broker = broker
        self.logger = logger
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
            self.logger.log(log_entry)
            print(f'[PV] Logged: {log_entry}')

        self.broker.consume(callback)
