from microbit import *

class Single_Relay():

    def __init__(self, set:MicroBitAnalogDigitalPin):
        self.set = set

    def on (self)->None:
        self.set.write_digital(1)

    def off (self)->None:
        self.set.write_digital(0)

