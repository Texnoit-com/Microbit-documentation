from microbit import MicroBitAnalogDigitalPin


class Analog_Temperature():

    def __init__(self, set: MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal(self) -> int:
        return self.set.read_analog()
