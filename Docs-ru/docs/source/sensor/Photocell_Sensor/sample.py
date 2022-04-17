from microbit import display, pin0

from Photocell import Photocell

photo = Photocell(pin0)

while True:
    display.scroll(photo.get_signal())
