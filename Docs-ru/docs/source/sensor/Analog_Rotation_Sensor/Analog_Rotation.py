from microbit import MicroBitAnalogDigitalPin


class Analog_Rotation():

    def __init__(self, value:MicroBitAnalogDigitalPin):
        self.value = value

    def get_signal (self)->int:
        return self.value.read_analog()

    def get_angle (self, max_signal = 1024)->int:
        degree = max_signal/180
        return self.value.read_analog()//degree
    
    def get_scale (self, max_signal = 1024, scale=10)->int:
        segment = max_signal/scale
        return self.value.read_analog()//segment
