from microbit import *


class Reed_Switch():

    def __init__(self, set: MicroBitAnalogDigitalPin,
                 count: int = 0):
        self.set = set
        self.count = count

    def is_pressed(self) -> bool:
        if self.set.read_analog() > 10:
            self.count += 1
            return True
        return False

    def reset_pressed(self) -> None:
        self.count = 0

    def count_pressed(self) -> int:
        return self.count
