from microbit import MicroBitAnalogDigitalPin

class Hall_Magnetic():

    def __init__(self, set:MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal (self)->int:
        return self.set.read_analog()

    def get_status (self, base_status:int)->bool:
        return False if (base_status-50 < self.set.read_analog() < base_status+50) else True
    