from microbit import Image, MicroBitAnalogDigitalPin, button_a, display, sleep


class Analog_Alcohol:

    ACCOUNT: int = 9

    def __init__(self, set_pin: MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def calibrate(self) -> None:
        animation = [Image("00900:00900:99999:00900:00900"),
                     Image("90009:09090:00900:09090:90009"),
                     Image("00000:00000:00900:00000:00000")]
        for i in range(self.ACCOUNT):
            display.show(self.ACCOUNT-i)
            sleep(1000)
            display.show(Image("00000:00900:00000:00900:00000"))
            sleep(1000)
        while not button_a.is_pressed():
            display.show(animation, delay=500)
        display.show(Image.YES)
        display.scroll(self.set_pin.read_analog())

    def get_signal(self) -> int:
        return self.set_pin.read_analog()
