from Ultrasonic import Ultrasonic
from microbit import sleep, display


sonar = Ultrasonic()
while  True :
     display.scroll(str(sonar.distance_mm () / 10 ))
     sleep ( 1000 )