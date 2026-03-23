"""Controller script for TutorialSensor."""
import time
from constellation.core.controller import ScriptableController

ctrl = ScriptableController(group="test", name="SensorCtrl", log_level="INFO")
time.sleep(1)

print("Satellites:", ctrl.constellation.satellites)
print("States:", ctrl.states)

print("\nInitializing...")
print(ctrl.command(cmd="initialize", sat="Sensor1", satcls="TutorialSensor", 
                   payload={"target_temperature": 30.0, "sample_rate": 2.0, "noise": 0.3}))
time.sleep(2)

print("\nLaunching...")
print(ctrl.command(cmd="launch", sat="Sensor1", satcls="TutorialSensor"))
time.sleep(2)

print("\nStarting...")
print(ctrl.command(cmd="start", sat="Sensor1", satcls="TutorialSensor", payload="calibration_001"))
time.sleep(12)  # Let it run for ~20 samples at 2Hz

print("\nStopping...")
print(ctrl.command(cmd="stop", sat="Sensor1", satcls="TutorialSensor"))
time.sleep(2)

print("\nFinal states:", ctrl.states)
