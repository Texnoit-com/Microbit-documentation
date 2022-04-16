from microbit import *
from neopixel import NeoPixel

np = NeoPixel(pin0, 5)
while True:
    for i in range(5):
        np[i] = (255, 0, 0)
        np.show()
        sleep(1000)
        np.clear()
