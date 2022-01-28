from microbit import *
import music

class Active_Buzzer():
    
    def __init__(self, set_pin=pin0):
        self.set_pin=set_pin
    
    def beep(self, stop_time:int)->None:
        t = running_time()
        while running_time()< t+stop_time:
            self.set_pin.write_digital(1)
        music.stop(self.set_pin)

    def siren(self, stop_time:int)->None:
        t = running_time()
        while running_time()< t+stop_time:
            self.set_pin.write_analog(500)
            sleep(500)
            self.set_pin.write_analog(1000)
            sleep(500)
        music.stop(self.set_pin)

    def play(self, melody)->None:
        music.play(melody,pin=self.set_pin, loop=True)

    def play_time(self, melody, stop_time:int)->None:
        t = running_time()
        while running_time()< t+stop_time:
            music.play(melody,pin=self.set_pin, loop=True)
        music.stop(self.set_pin)

    def stop(self):
        music.stop(self.set_pin)
