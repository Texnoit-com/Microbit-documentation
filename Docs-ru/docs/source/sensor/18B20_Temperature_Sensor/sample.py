from microbit import *

from B20_Temperature import B20_Temperature

temp = B20_Temperature(pin0)

while True:

    display.scroll(temperature())
    sleep(1000)
    display.scroll(temp.temperature())
    sleep(1000)
