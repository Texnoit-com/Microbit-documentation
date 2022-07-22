from microbit import sleep


class Capacitive_Touch():

    PAUSE: int = 10

    def __init__(self, set_pin):
        self.set_pin = set_pin
        self.count = 0

    def is_pressed(self) -> bool:
        if self.set_pin.read_analog() > self.PAUSE:
            self.count += 1
            return True
        return False

    def click(self, time: int) -> bool:
        if self.set_pin.read_analog() > self.PAUSE:
            sleep(time)
            if self.set_pin.read_analog() < self.PAUSE:
                self.count += 1
                return True
        return False

    def reset_pressed(self) -> None:
        self.count = 0

    def count_pressed(self) -> int:
        return self.count
