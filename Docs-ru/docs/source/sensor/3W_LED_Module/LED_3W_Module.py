from microbit import MicroBitAnalogDigitalPin


class LED_3W_Module():

    def __init__(self, value:MicroBitAnalogDigitalPin):
        self.value = value

    def on (self)->None:
        self.value.write_digital(1)

    def off (self)->None:
        self.value.write_digital(0)

    def bright (self, arg:int)->None:
        self.value.write_analog(arg)
