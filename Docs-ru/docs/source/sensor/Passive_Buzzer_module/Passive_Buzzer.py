import music
from microbit import *


class Passive_Buzzer():
    
    def __init__(self, set_pin: MicroBitAnalogDigitalPin=pin0):
        self.set_pin = set_pin
    
    def play(self, melody) -> None:
        music.play(melody, pin=self.set_pin)

    def play_time(self, melody, stop_time:int) -> None:
        t = running_time()
        music.play(melody, pin=self.set_pin, wait=False)
        while running_time() < t+stop_time:
            sleep(100)
        music.stop(self.set_pin)

    def stop(self) -> None:
        music.stop(self.set_pin)
