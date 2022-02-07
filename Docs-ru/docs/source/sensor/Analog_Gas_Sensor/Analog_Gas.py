from microbit import *

class Analog_Gas:

    def __init__(self, set_pin:MicroBitAnalogDigitalPin):
        self.set_pin = set_pin
    
    def calibrate(self):
        animation=[Image("00900:00900:99999:00900:00900"),
                   Image("90009:09090:00900:09090:90009"),
                   Image("00000:00000:00900:00000:00000"),
                   Image("00000:09990:09990:09990:00000"),
                   Image("00000:00000:00900:00000:00000"),
                   Image("00900:09090:09990:09090:09090")
                  ]
        while button_a.is_pressed():            
            display.show(animation, delay=500)
        

    def get_signal(self):
        return self.set_pin.read_analog()