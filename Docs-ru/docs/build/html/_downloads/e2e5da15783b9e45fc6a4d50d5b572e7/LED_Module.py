class LED_Module():

    def __init__(self, setpin):
        self.setpin = setpin

    def on(self) -> None:
        self.setpin.write_digital(1)

    def off(self) -> None:
        self.setpin.write_digital(0)

    def bright(self, arg: int) -> None:
        self.setpin.write_analog(arg)
