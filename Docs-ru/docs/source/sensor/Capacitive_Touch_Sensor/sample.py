from microbit import Image, display, pin0, sleep

from Capacitive_Touch import Capacitive_Touch

touch = Capacitive_Touch(pin0)

while True:
    if touch.is_pressed():
        display.show(Image.YES)
        break
    sleep(200)
