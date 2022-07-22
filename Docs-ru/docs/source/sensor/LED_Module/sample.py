from LED_Module import LED_Module
from microbit import *

led1 = LED_Module(pin0)

led1.on()
sleep(1000)
led1.off()
