from microbit import *


class Vibration:

    def __init__(self, set_pin: MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def calibrate(self) -> None:
        pass

    def get_signal(self) -> int:
        return self.set_pin.read_analog()
