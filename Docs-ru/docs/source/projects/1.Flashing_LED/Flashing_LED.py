from LED_3W_Module import LED_3W_Module
from microbit import pin0, sleep

led1 = LED_3W_Module(pin0)
while True:
    led1.on()
    sleep(500)
    led1.off()
    sleep(500)
