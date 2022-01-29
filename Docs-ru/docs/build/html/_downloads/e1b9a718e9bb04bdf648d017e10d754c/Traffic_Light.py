from microbit import *
from random import randint

class Traffic_Light():
    
    def __init__(self, 
                    red:MicroBitDigitalPin, 
                    yellow:MicroBitDigitalPin, 
                    green:MicroBitDigitalPin):
        self.red = red
        self.yellow = yellow
        self.green = green
    
    def off (self)->None:
        self.red.write_digital(0)
        self.green.write_digital(0)
        self.yellow.write_digital(0)

    def on_red (self)->None:
        self.red.write_digital(1)

    def off_red (self)->None:
        self.red.write_digital(0)

    def on_green (self)->None:
        self.green.write_digital(1)

    def off_green (self)->None:
        self.green.write_digital(0)
    
    def on_yellow (self)->None:
        self.yellow.write_digital(1)

    def off_yellow (self)->None:
        self.yellow.write_digital(0)
