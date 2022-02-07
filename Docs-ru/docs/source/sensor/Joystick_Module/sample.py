from microbit import *
from Joystick import Joystick

joys=Joystick(pin0, pin1, pin2)

while  True :
     display.scroll(joys.play_diagonal())
     sleep ( 100 )
