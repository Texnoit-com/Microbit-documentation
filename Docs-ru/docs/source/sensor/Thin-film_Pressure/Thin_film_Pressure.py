class Thin_film_Pressure:

    def __init__(self, set_pin):
        self.set_pin = set_pin

    def get_signal(self) -> int:
        return self.set_pin.read_analog()
