from microbit import MicroBitAnalogDigitalPin


class Digital_Tilt:

    PAUSE: int = 600
    def __init__(self, set_pin: MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def vibration(self):
        if self.set_pin.read_analog() < self.PAUSE:
            return True
        return False
