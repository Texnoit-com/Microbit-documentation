from microbit import display, pin0

from Analog_Sound import Analog_Sound

mic = Analog_Sound(pin0)
mic.calibrate()
while True:
    display.show(mic.count_claps())
