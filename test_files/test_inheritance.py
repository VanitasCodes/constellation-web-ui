import time
from constellation.core.controller import ScriptableController
from constellation.core.listener import MonitoringListener

class WebBridgeController(ScriptableController, MonitoringListener):
    def __init__(self, group, **kwargs):
        print("Initializing WebBridgeController...")
        super().__init__(group=group, **kwargs)
        print("Setting topics...")
        self.set_topics(["LOG/", "STAT/"])

    def receive_log(self, record):
        print(f"LOG: [{record.levelname}] {getattr(record, 'sender', record.name)} :: {record.getMessage()}")

    def receive_metric(self, sender, metric, time, value):
        print(f"METRIC: {sender} {metric.name} = {value} {metric.unit}")

print("Creating controller...")
ctrl = WebBridgeController(group="test", name="WebBridge", log_level="INFO")

print("\nDiscovered satellites:")
print(ctrl.constellation.satellites)

print("\nStates:")
print(ctrl.states)

print("\nSending initialize...")
print(ctrl.command(cmd="initialize", sat="Sat1", satcls="PyRandomTransmitter", payload={}))
time.sleep(2)

print("\nSending launch...")
print(ctrl.command(cmd="launch", sat="Sat1", satcls="PyRandomTransmitter", payload=None))
time.sleep(2)

print("\nSending start...")
print(ctrl.command(cmd="start", sat="Sat1", satcls="PyRandomTransmitter", payload="run_001"))

print("\nWaiting 20 seconds for logs and metrics in RUN state...")
time.sleep(20)

print("\nFinal states:")
print(ctrl.states)
