from microbit import display, pin0

from Water import Water

wat = Water(pin0)

while True:
    display.scroll(wat.get_signal())
