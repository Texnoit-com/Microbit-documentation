from microbit import pin0, pin1, pin13, pin14, pin15, pin16

from Motor import Motor

l_motor = Motor(pin13, pin14, pin0)
r_motor = Motor(pin15, pin16, pin1)

while True:
    l_motor.forward(500)
    r_motor.forward(500)
