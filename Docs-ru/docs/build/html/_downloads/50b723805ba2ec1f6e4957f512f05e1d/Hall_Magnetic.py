from microbit import *

class Hall_Magnetic():

    def __init__(self, set:MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal (self)->int:
        return self.set.read_analog()

    def get_status (self, base_status:int, span=20)->bool:
        return True if (base_status-span < self.set.read_analog() < base_status+span) else False
    