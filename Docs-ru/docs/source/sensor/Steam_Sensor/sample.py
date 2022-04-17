from microbit import display, pin0

from Steam import Steam

steam_1 = Steam(pin0)

while True:
    display.scroll(steam_1.get_signal())
