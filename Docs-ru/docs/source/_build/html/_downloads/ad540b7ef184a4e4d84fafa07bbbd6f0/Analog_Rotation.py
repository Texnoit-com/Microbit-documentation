from microbit import MicroBitAnalogDigitalPin

class Analog_Rotation():

    def __init__(self, set:MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal (self)->int:
        return self.set.read_analog()

    def get_angle (self, max_signal = 1024)->int:
        degree = max_signal/180
        return self.set.read_analog()//degree
    
    def get_scale (self, max_signal = 1024, scale=10)->int:
        segment = max_signal/scale
        return self.set.read_analog()//segment