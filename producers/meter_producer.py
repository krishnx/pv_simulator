import time
from interfaces.i_producer import IProducer
from services.simulator import MeterSimulatorService


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
            print(f'[Meter] Sent: {message}')
            time.sleep(2)
