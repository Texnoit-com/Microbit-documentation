from microbit import *

class Analog_Sound:

    def __init__(self, set_pin:MicroBitAnalogDigitalPin):
        self.set_pin = set_pin

    def calibrate(self):
        t = running_time()
        last_time = t
        prev = 0
        calibrated = False
        while not calibrated:
            r = self.set_pin.read_analog()
            r = abs(r)/450*5 
            r = int(r) if r < 6 else 5
            if (r == 5 and prev != 5) or (r == 0 and prev != 0):
                t = running_time()
            prev = r
            if running_time() - t > 3000:
                last_time = running_time()
                if r == 0:
                    display.show(Image.ARROW_E)
                else: 
                    display.show(Image.ARROW_W)
            else:
                for y in range(0, 5):
                    for x in range(0, 5):
                        if 4 - y < r:
                            display.set_pixel(x, y, 5)
                        else:
                            display.set_pixel(x, y, 0)
                if r > 0:
                    sleep(100)
                if running_time() - last_time > 5000:
                    display.show(Image.YES)
                    sleep(1000)
                    calibrated = True
                    display.clear()
        return calibrated

    def level_sound(self):
        return self.set_pin.read_analog()

    def count_claps(self,sleep_time=100):
        t = running_time()
        lastr = 5
        claps = 0
        while running_time() - t < 500:
            r = self.set_pin.read_analog()
            if lastr > 5 and r < 1:
                t = running_time()
                sleep(sleep_time)
            elif lastr < 1 and r > 5:
                t = running_time()
                sleep(sleep_time)
                claps += 1
            lastr = r
        return claps