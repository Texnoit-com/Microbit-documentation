from microbit import Image, display, pin0

from Digital_Tilt import Digital_Tilt

tilt = Digital_Tilt(pin0)

while True:
    if tilt.vibration():
        display.show(Image.YES)
