from microbit import *
from Driver_Motor import Driver_Motor, Motor

l_motor=Motor(pin13,pin14,pin0)
r_motor=Motor(pin15,pin16,pin1)

car = Driver_Motor(l_motor,r_motor)

speed = 500

car.forward(speed)
sleep(1000)

car.backward(speed)
sleep(1000)

car.left_tank(speed)
sleep(500)
