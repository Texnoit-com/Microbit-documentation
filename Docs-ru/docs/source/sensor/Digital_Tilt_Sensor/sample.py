from microbit import *
from Digital_Tilt import  Digital_Tilt

tilt= Digital_Tilt(pin0)

while True:
     if tilt.vibration():
         display.show(Image.YES)
