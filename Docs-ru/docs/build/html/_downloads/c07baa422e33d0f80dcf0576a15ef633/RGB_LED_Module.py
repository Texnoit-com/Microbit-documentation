from random import randint

from microbit import sleep


class RGB_LED_Module():

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def off(self) -> None:
        self.red.write_digital(0)
        self.green.write_digital(0)
        self.blue.write_digital(0)

    def on_red(self) -> None:
        self.red.write_digital(1)

    def off_red(self) -> None:
        self.red.write_digital(0)

    def bright_red(self, arg: int) -> None:
        self.red.write_analog(arg)

    def on_green(self) -> None:
        self.green.write_digital(1)

    def off_green(self) -> None:
        self.green.write_digital(0)

    def bright_green(self, arg: int) -> None:
        self.green.write_analog(arg)

    def on_blue(self) -> None:
        self.blue.write_digital(1)

    def off_blue(self) -> None:
        self.rblue.write_digital(0)

    def bright_blue(self, arg: int) -> None:
        self.blue.write_analog(arg)

    def conversion(self, start, finish, time: int) -> None:
        for i in range(1023):
            start.write_analog(1023-i)
            finish.write_analog(i)
            sleep(int(time/1023))

    def random_rgb(self, time: int, step=10) -> None:
        while time > 0:
            self.red.write_analog(randint(0, 100)*10)
            self.green.write_analog(randint(0, 100)*10)
            self.blue.write_analog(randint(0, 100)*10)
            sleep(step)
            time -= step
