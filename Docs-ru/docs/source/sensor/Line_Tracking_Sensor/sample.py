from microbit import *

from Line_Tracking import Line_Tracking

line = Line_Tracking(pin0)

line.calibrate()
while True:
     display.scroll(line.get_signal())
