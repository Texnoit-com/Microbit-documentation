from microbit import display, pin0

from Flame import Flame

fire = Flame(pin0)

fire.calibrate()
while True:
    display.scroll(fire.get_signal())
