from microbit import *

class Analog_Alcohol:

    def __init__(self, set_pin:MicroBitAnalogDigitalPin):
        self.set_pin = set_pin
    
    def calibrate(self):
        pass

    def get_signal(self):
        return self.set_pin.read_analog()