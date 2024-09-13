class ControlCircuit:
    def __init__(self, resistance, voltage):
        self.resistance = resistance
        self.voltage = voltage

    def calculate_current(self):
        return self.voltage / self.resistance

circuit = ControlCircuit(10, 230)
print(f"Current: {circuit.calculate_current()} A")
