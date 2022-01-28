from microbit import *
import music

class Passive_Buzzer():
    
    def __init__(self, set_pin=pin0):
        self.set_pin=set_pin
    
    def play(self, melody)->None:
        music.play(melody,pin=self.set_pin, loop=True)

    def play_time(self, melody, stop_time:int)->None:
        t = running_time()
        while running_time()< t+stop_time:
            music.play(melody,pin=self.set_pin, loop=True)
        music.stop(self.set_pin)

    def stop(self):
        music.stop(self.set_pin)