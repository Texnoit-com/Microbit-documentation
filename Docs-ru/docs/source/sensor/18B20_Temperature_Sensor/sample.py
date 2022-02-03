from microbit import *
from B20_Temperature import B20_Temperature

temp=B20_Temperature(pin0)

display.scroll(str(temp.get_signal()))
sleep(1000)