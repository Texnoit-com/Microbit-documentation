from microbit import *


class Micro_Servo:
    def __init__(self, set_pin: MicroBitAnalogDigitalPin,
                 period: int = 20):
        self.set_pin = set_pin
        self.period = period
        self.set_pin.set_analog_period(self.period)

    def set_ms_pulse(self, ms: float) -> float:
        self.set_pin.write_analog(1023*ms/20)

    def angle(self, arg: int) -> None:
       self.set_ms_pulse(arg/60)
