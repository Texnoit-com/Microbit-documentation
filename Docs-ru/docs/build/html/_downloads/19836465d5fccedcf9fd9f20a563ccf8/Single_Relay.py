class Single_Relay():

    def __init__(self, set_pin):
        self.set = set

    def on(self) -> None:
        self.set.write_digital(1)

    def off(self) -> None:
        self.set.write_digital(0)
