from microbit import display, pin0

from Thin_film_Pressure import Thin_film_Pressure

pressure = Thin_film_Pressure(pin0)

while True:
    display.scroll(pressure.get_signal())
