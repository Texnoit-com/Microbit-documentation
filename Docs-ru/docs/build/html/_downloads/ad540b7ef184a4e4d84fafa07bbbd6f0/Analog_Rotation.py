from microbit import MicroBitAnalogDigitalPin


class Analog_Rotation():

    ANGLE: int = 180
    SCALE: int = 1024

    def __init__(self, set: MicroBitAnalogDigitalPin):
        self.set = set

    def get_signal(self) -> int:
        return self.set.read_analog()

    def get_angle(self, max_signal=SCALE) -> int:
        degree = max_signal/self.ANGLE
        return self.set.read_analog()//degree

    def get_scale(self, max_signal=SCALE, size=10) -> int:
        segment = max_signal/size
        return self.set.read_analog()//segment
