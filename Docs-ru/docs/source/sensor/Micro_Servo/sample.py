from microbit import button_a, pin0, sleep

from Micro_Servo import Micro_Servo

servo = Micro_Servo(pin0)

while True:
    if button_a.was_pressed():
        for i in range(180):
            servo.angle(i)
            sleep(10)
