from microbit import *
from Flame import  Flame

fire= Flame(pin0)

fire.calibrate()
while True:
     display.scroll(fire.get_signal())