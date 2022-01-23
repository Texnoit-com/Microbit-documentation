from Ultrasonic import Ultrasonic
from microbit import sleep, button_a, display


sonar = Ultrasonic()
while  True :
     print ( '%.1f'  % ( sonar.distance_mm () / 10 ))
     sleep ( 1000 )