from microbit import spi
from microbit import pin13, pin14, pin15


class Ultrasonic:

    def __init__(self, trigger=pin15, echo=pin14, sclk=pin13):
        self.trigger = trigger
        self.echo = echo
        self.sclk = sclk

    def distance_mm(self) -> int:
        spi.init(baudrate=125000, sclk=self.sclk,
                 mosi=self.trigger_pin, miso=self.echo)
        pre = 0 # убрать
        post = 0 # убрать
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)

        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        
        if i > 0:
            pre = bin(value).count("1")
            
            try:
                k, value = next((ind, v)
                                for ind, v in enumerate(resp[i:length - 2]) if resp[i + ind + 1] == 0)
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1

        dist= -1 if i < 0 else round(((pre + (k - i) * 8. + post) * 8 * 0.172) / 2)
        return dist