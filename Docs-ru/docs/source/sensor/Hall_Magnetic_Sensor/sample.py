from microbit import *
from Hall_Magnetic import Hall_Magnetic

magnetic=Hall_Magnetic(pin0)

while True:
    display.scroll(str(magnetic.get_signal()))
    sleep(1000)

    if magnetic.get_status(16,10):
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(1000)
