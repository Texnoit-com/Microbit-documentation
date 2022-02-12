from microbit import *
from Analog_Gas import Analog_Gas

gas=Analog_Gas(pin0)

gas.calibrate()
while True:
     display.scroll(gas.get_signal())