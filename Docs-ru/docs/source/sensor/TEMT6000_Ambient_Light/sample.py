from microbit import display, pin0, sleep

from TEMT import TEMT

temp = TEMT(pin0)

while True:
    display.scroll(temp.get_signal())
    sleep(1000)
