from microbit import MicroBitAnalogDigitalPin


class LED_Module():

    def __init__(self, set: MicroBitAnalogDigitalPin):
        self.set = set

    def on(self) -> None:
        self.set.write_digital(1)

    def off(self) -> None:
        self.set.write_digital(0)

    def bright(self, arg: int) -> None:
        self.set.write_analog(arg)
