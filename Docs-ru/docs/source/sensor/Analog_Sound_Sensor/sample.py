from AnalogSound import AnalogSound
from microbit import pin0

mic=AnalogSound(pin0)
mic.calibrate()
print("Calibrated")
while True:
    print(mic.count_claps())