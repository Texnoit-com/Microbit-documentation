from microbit import *

from RGB_LED_Module import RGB_LED_Module

led = RGB_LED_Module(pin0, pin1, pin2)


led.random_rgb(3000, 100)
sleep(2000)

led.conversion(led.red, led.green, 3000)
sleep(2000)

led.conversion(start=led.red, finish=led.green, time=3000) # можно использовать явную передачу параметров
