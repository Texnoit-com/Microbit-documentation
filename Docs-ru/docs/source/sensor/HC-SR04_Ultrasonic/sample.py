from microbit import display, pin1, pin2, sleep

from Ultrasonic import Ultrasonic

sonar = Ultrasonic(pin2, pin1)

while True:
    display.scroll(int(sonar.distance_mm()))
    sleep(1000)
