from microbit import Image, button_a, display


class Line_Tracking:

    PAUSE: int = 500

    def __init__(self, set_pin):
        self.set_pin = set_pin

    def calibrate(self):
        animation = [Image("00900:00900:99999:00900:00900"),
                     Image("90009:09090:00900:09090:90009"),
                     Image("00000:00000:00900:00000:00000")]
        while not button_a.is_pressed():
            display.show(animation, delay=self.PAUSE)
        display.show(Image.YES)
        display.scroll(self.set_pin.read_analog())

    def get_signal(self):
        return self.set_pin.read_analog()
