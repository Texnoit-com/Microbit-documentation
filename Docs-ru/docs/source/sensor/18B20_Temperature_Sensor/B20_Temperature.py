from microbit import *

class B20_Temperature():

    def __init__(self, set:MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal (self)->int:
        return self.set.read_analog()
    
    def temperature (self)->int:
        return int(self.set.read_analog()/3)