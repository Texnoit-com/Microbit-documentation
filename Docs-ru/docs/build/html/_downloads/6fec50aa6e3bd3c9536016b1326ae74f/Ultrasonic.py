from microbit import *
from machine import time_pulse_us

class Ultrasonic:
    def __init__(self, trig_pin:MicroBitDigitalPin, echo_pin:MicroBitDigitalPin, speed_sound = 34300):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.trig_pin.write_digital(1)
        self.echo_pin.read_digital()
        self.speed_sound = speed_sound
        self.microsecinds = 1000000
    
    def distance_cm(self):
        self.trig_pin.write_digital(1)
        self.trig_pin.write_digital(0)
        self.signal = time_pulse_us(self.echo_pin, 1) / self.microsecinds
        self.dist = (self.signal/2) * self.speed_sound
        return int(self.dist)
    
    def distance_mm(self):
        self.trig_pin.write_digital(1)
        self.trig_pin.write_digital(0)
        self.signal = time_pulse_us(self.echo_pin, 1) / self.microsecinds
        self.dist = (self.signal/2) * self.speed_sound
        return int(self.dist*10)
