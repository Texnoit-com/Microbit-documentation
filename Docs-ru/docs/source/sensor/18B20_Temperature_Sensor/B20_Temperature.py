class B20_Temperature():

    def __init__(self, set_pin):
        self.set_pin = set_pin

    def get_signal(self) -> int:
        return self.set_pin.read_analog()

    def temperature(self) -> int:
        return int(self.set_pin.read_analog()/3)
