from microbit import *


class Digital_Tilt:

    def __init__(self, set_pin: MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def vibration(self):
        if self.set_pin.read_analog() < 600:
            return True
        return False
