from Analog_Sound import Analog_Sound
from microbit import *

mic=AnalogSound(pin0)
mic.calibrate()
while True:
    display.show(mic.count_claps())
