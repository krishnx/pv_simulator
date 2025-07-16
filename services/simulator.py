import math
from datetime import datetime, timezone
import random


class PVSimulatorService:
    """
    Simulates a photovoltaic (PV) power generation based on the time of day.
    """
    MAX_PV_POWER = 10.0  # Upper limit for the PV power generation in kW

    def simulate(self):
        # Calculate time of day as a fraction (0.0 to 1.0)
        # Shift to make 0.5 (midday) the peak for a sine wave
        current_time = datetime.now(timezone.utc)
        hour_of_day = current_time.hour + current_time.minute / 60.0

        # Simple bell curve approximation using sine function
        # Sine wave from -pi/2 to pi/2 over 24 hours, shifted to peak at 12:00
        # The period is 24 hours, so 2*pi/24
        # Offset by -6 hours to make 12:00 (hour 12) the peak of the sine wave
        # sin((hour - 6) * pi / 12) will go from 0 (6am) to 1 (12pm) to 0 (6pm)

        # Ensure power is only generated during "daylight" hours (e.g., 6 AM to 6 PM)
        if 6 <= hour_of_day <= 18:
            # Scale hour_of_day to be between 0 and 1 for the bell curve
            # 6 AM is 0, 12 PM is 0.5, 6 PM is 1
            scaled_time = (hour_of_day - 6) / 12.0

            # Use a sine function for a smooth bell curve effect
            # math.sin(scaled_time * math.pi) goes from 0 (at 0) to 1 (at 0.5) to 0 (at 1)
            pv_power = self.MAX_PV_POWER * math.sin(scaled_time * math.pi)
            return round(max(0.0, pv_power), 2)
        else:
            return 0.0  # No PV power at night


class MeterSimulatorService:
    """
    Simulates a meter reading that fluctuates randomly between 0.0 and 10.0.
    """
    METER_UPPER_LIMIT = 10.0  # Upper limit for the meter reading in kW

    def simulate(self):
        return round(random.uniform(0.0, self.METER_UPPER_LIMIT), 2)
