from microbit import *
from Crash_Sensor import Crash_Sensor

crash=Crash_Sensor(pin0)

while True:
    if crash.is_pressed():
        display.show(crash.count_pressed())
    if crash.count_pressed()>3:
        crash.reset_pressed()
        break
    sleep(200)
display.show(crash.count_pressed())
