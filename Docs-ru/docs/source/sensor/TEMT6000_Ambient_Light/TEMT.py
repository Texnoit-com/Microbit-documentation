from microbit import *


class TEMT():

    def __init__(self, value: MicroBitAnalogDigitalPin):
        self.value = value

    def get_signal(self) -> int:
        return self.value.read_analog()
