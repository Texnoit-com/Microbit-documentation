class Reed_Switch():

    def __init__(self, set_pin):
        self.set_pin = set_pin
        self.count = 0

    def is_pressed(self) -> bool:
        if self.set_pin.read_analog() > 10:
            self.count += 1
            return True
        return False

    def reset_pressed(self) -> None:
        self.count = 0

    def count_pressed(self) -> int:
        return self.count
