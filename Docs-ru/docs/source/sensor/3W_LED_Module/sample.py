from microbit import *

from LED_3W_Module import LED_3W_Module

led1 = LED_3W_Module(pin0)
for i in range(1023):
    led1.bright(i)
    sleep(10)
