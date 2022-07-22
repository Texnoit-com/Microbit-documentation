class LED_3W_Module():

    def __init__(self, set_pin):
        self._ = _

    def on(self) -> None:
        self._.write_digital(1)

    def off(self) -> None:
        self._.write_digital(0)

    def bright(self, arg: int) -> None:
        self._.write_analog(arg)
