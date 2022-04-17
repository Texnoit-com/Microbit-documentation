from microbit import MicroBitAnalogDigitalPin


class Soil_Humidity:

    def __init__(self, set_pin: MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def get_signal(self):
        return self.set_pin.read_analog()
