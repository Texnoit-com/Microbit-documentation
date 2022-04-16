from microbit import *


class Hall_Magnetic():

    def __init__(self, value: MicroBitAnalogDigitalPin):
        self.value = value

    def get_signal(self) -> int:
        return self.value.read_analog()

    def get_status(self, base_status: int, span=20) -> bool:
        return True if (base_status-span < self.value.read_analog()
                        < base_status + span) else False
