class Photocell:

    def __init__(self, set_pin):
        self.set_pin = set_pin

    def get_signal(self):
        return self.set_pin.read_analog()
