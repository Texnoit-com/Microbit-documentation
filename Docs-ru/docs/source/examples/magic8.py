'''Программа волшебный шар.'''


from random import choice

from microbit import accelerometer, display, sleep

answers = ['Yes', 'No', 'Аsk more']

while True:
    display.show('8')
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.scroll(choice(answers))
    sleep(10)
