from microbit import *


class Single_Relay():

    def __init__(self, value: MicroBitAnalogDigitalPin):
        self.value = value

    def on(self) -> None:
        self.value.write_digital(1)

    def off(self) -> None:
        self.value.write_digital(0)
