class Micro_Servo:

    SCALE: int = 1023
    SPAN: int = 20
    AGAIL: int = 60

    def __init__(self, set_pin, period=20):
        self.set_pin = set_pin
        self.period = period
        self.set_pin.set_analog_period(self.period)

    def set_ms_pulse(self, ms: float):
        self.set_pin.write_analog(self.SCALE*ms/self.SPAN)

    def angle(self, arg: int):
        return self.set_ms_pulse(arg/self.AGAIL)
