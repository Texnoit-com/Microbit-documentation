from microbit import *


class Crash_Sensor():

    def __init__(self, value:MicroBitAnalogDigitalPin):
        self.value = value
        self.count=0

    def is_pressed(self)->bool:
        if self.value.read_analog() < 10:
            self.count += 1
            return True
        return False

    def click(self, time:int)->bool:
        if self.value.read_analog() < 10:
            sleep(time)
            if self.value.read_analog() > 10:
                self.count += 1
                return True
        return False

    def revalue_pressed(self)->None:
        self.count=0

    def count_pressed(self)->int:
        return self.count
