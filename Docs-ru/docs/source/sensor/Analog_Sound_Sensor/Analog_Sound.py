from microbit import pin0, display, sleep, running_time, Image


class AnalogSound:

    def __init__(self, set_pin=pin0):
        self.set_pin = set_pin

    def calibrate(self):
        t = running_time()
        last_time = t
        prev = 0
        calibrated = False
        while not calibrated:
            r = self.set_pin.read_analog()-11
            r = abs(r)/900*5
            r = int(r) if r < 6 else 5
            if (r == 5 and prev != 5) or (r == 0 and prev != 0):
                t = running_time()
            prev = r
            if running_time() - t > 3000:
                lastrt = running_time()
                if r == 0:  # No sound for more than 3 seconds
                    # Turn right
                    display.show(Image.ARROW_E)
                else:  # Saturated for more than 3 seconds
                    # Turn left
                    display.show(Image.ARROW_W)
            else:
                for y in range(0, 5):
                    for x in range(0, 5):
                        if 4 - y < r:
                            display.set_pixel(x, y, 5)
                        else:
                            display.set_pixel(x, y, 0)
                if r > 0:
                    # If there is sound, leave the leds on for .1 seconds
                    sleep(100)
                if running_time() - lastrt > 5000:
                    display.show(Image.YES)
                    sleep(1000)
                    calibrated = True
                    display.clear()
        return calibrated

    def level_sound(self):
        pass

    def count_claps(self):
        t = running_time()
        lastr = 900
        claps = 0
        while running_time() - t < 1000:
            r = self.set_pin.read_analog()
            if lastr > 500 and r < 100:
                t = running_time()
                sleep(100)
            elif lastr < 100 and r > 500:
                t = running_time()
                sleep(100)
                claps += 1
            lastr = r
        return claps