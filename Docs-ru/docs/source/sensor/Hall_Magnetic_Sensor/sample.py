from microbit import *
from Hall_Magnetic import Hall_Magnetic

magnetic=Hall_Magnetic(pin0)

display.scroll(str(magnetic.get_signal()))
sleep(1000)

if magnetic.base_status(300):
     display.scroll(Image.YES)
sleep(1000)