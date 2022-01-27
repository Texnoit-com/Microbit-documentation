from microbit import sleep, display
from Ultrasonic import Ultrasonic


sonar = Ultrasonic()
while  True :
     display.scroll(str(sonar.distance_mm () / 10 ))
     sleep ( 1000 )
