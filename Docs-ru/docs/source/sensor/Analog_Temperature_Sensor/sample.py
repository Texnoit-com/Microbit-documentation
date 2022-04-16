from microbit import *
from Analog_Temperature import Analog_Temperature

temp=Analog_Temperature(pin0)

display.scroll(str(temp.get_signal()))
sleep(1000)
