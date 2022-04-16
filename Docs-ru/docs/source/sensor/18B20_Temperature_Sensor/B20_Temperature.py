from microbit import MicroBitAnalogDigitalPin


class B20_Temperature():

    def __init__(self, value:MicroBitAnalogDigitalPin):
        self.value = value

    def get_signal (self)->int:
        return self.value.read_analog()
    
    def temperature (self)->int:
        return int(self.value.read_analog()/3)
