import time
import random
from constellation.core.satellite import Satellite, SatelliteArgumentParser
from constellation.core.configuration import Configuration
from constellation.core.logging import setup_cli_logging
from constellation.core.monitoring import schedule_metric


class TutorialSensor(Satellite):
    """A simulated temperature sensor satellite."""

    def __init__(self, *args, **kwargs):
        self._temperature = 20.0
        self._measuring = False
        self._sample_count = 0
        super().__init__(*args, **kwargs)

    @schedule_metric(unit="°C", interval=2.0)
    def temperature(self):
        """Current temperature reading."""
        if self._measuring:
            return self._temperature
        return None

    @schedule_metric(unit="", interval=5.0)
    def sample_count(self):
        """Total samples taken."""
        if self._measuring:
            return self._sample_count
        return None

    def do_initializing(self, config: Configuration) -> str:
        """Read configuration parameters."""
        self._target_temp = config.get_float("target_temperature", 25.0, min_val=-40.0, max_val=200.0)
        self._sample_rate = config.get_float("sample_rate", 1.0, min_val=0.1, max_val=100.0)
        self._noise = config.get_float("noise", 0.5, min_val=0.0, max_val=10.0)
        self.log.info(f"Configured: target={self._target_temp}°C, rate={self._sample_rate}Hz, noise={self._noise}")
        return f"Initialized with target temperature {self._target_temp}°C"

    def do_launching(self) -> str:
        """Simulate powering up the sensor."""
        self.log.info("Powering up temperature sensor...")
        time.sleep(0.5)
        self._temperature = 20.0 + random.uniform(-1, 1)
        self.log.info(f"Sensor online, ambient temperature: {self._temperature:.1f}°C")
        return "Sensor powered up"

    def do_landing(self) -> str:
        """Simulate powering down the sensor."""
        self.log.info("Powering down temperature sensor...")
        self._measuring = False
        self._temperature = 20.0
        return "Sensor powered down"

    def do_starting(self, run_identifier: str) -> str:
        """Prepare for a measurement run."""
        self._sample_count = 0
        self._measuring = True
        self.log.info(f"Starting measurement run: {run_identifier}")
        return f"Started run {run_identifier}"

    def do_run(self, payload) -> str:
        """Main measurement loop."""
        self.log.info("Measurement loop running")
        while not self.stop_requested():
            self._temperature = self._target_temp + random.uniform(-self._noise, self._noise)
            self._sample_count += 1
            if self._sample_count % 10 == 0:
                self.log.info(f"Sample {self._sample_count}: {self._temperature:.2f}°C")
            time.sleep(1.0 / self._sample_rate)
        return f"Measurement complete, {self._sample_count} samples collected"

    def do_stopping(self) -> str:
        """Stop measurement."""
        self._measuring = False
        self.log.info(f"Stopped after {self._sample_count} samples")
        return f"Stopped, collected {self._sample_count} samples"

    def fail_gracefully(self) -> str:
        """Clean up on error."""
        self._measuring = False
        return "Failed gracefully, sensor safe"


def main(args=None):
    """Tutorial temperature sensor satellite."""
    parser = SatelliteArgumentParser(description=main.__doc__)
    args = vars(parser.parse_args(args))
    setup_cli_logging(args.pop("level"))
    s = TutorialSensor(**args)
    s.run_satellite()


if __name__ == "__main__":
    main()
