from microbit import pin0, pin1, pin2, sleep
from Traffic_Light import Traffic_Light

led1 = Traffic_Light(pin0, pin1, pin2)


while True:
    led1.on_red()
    sleep(10000)
    led1.off_red()
    led1.on_yellow()
    sleep(2000)
    led1.off_yellow()
    led1.on_green()
    sleep(10000)
    led1.off_green()
    led1.on_yellow()
    sleep(2000)
    led1.off_yellow()
