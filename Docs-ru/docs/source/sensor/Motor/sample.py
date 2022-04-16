from microbit import *
from Motor import Motor

l_motor=Motor(pin13,pin14,pin0)
r_motor=Motor(pin15,pin16,pin1)

while True:
     l_motor.forward(500)
     r_motor.forward(500)
