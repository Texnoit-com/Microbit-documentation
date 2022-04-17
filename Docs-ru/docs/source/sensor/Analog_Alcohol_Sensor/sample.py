from microbit import display, pin0

from Analog_Alcohol import Analog_Alcohol

alcohol = Analog_Alcohol(pin0)

alcohol.calibrate()
while True:
    display.scroll(alcohol.get_signal())
