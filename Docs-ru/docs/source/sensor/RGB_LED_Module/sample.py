from microbit import *
from RGB_LED_Module import RGB_LED_Module

led1=RGB_LED_Module(pin0,pin1,pin2)


while True:
     led1.random_rgb(3000,100)
