# Constellation API Tests

These files demonstrate the multiple inheritance approach and custom satellite creation described in the GSoC proposal.

**Requirements:** Constellation 0.7 installed (MR !1012 branch or later)

## Multiple Inheritance Test

`test_inheritance.py` — Tests `WebBridgeController(ScriptableController, MonitoringListener)`, the combined controller that handles commands, state tracking, and CMDP log/metric receiving through a single class.

```bash
# Terminal 1
SatellitePyRandomTransmitter -n Sat1 -g test

# Terminal 2
python test_inheritance.py
```

**Expected:** Discovers satellite, sends commands through full FSM cycle, receives CMDP log callbacks. Ends in ERROR state due to BOR timeout (expected — transmitter has no receiver).

## Custom Satellite

`tutorial_satellite.py` — A simulated temperature sensor demonstrating FSM transitions, configuration handling, and scheduled metrics.

`test_sensor.py` — Controller script that runs the sensor through a full measurement cycle.

```bash
# Terminal 1
python tutorial_satellite.py -n Sensor1 -g test

# Terminal 2
python test_sensor.py
```

**Expected:** Full cycle NEW → INIT → ORBIT → RUN (collecting samples at configured rate) → ORBIT. Final state is ORBIT.
