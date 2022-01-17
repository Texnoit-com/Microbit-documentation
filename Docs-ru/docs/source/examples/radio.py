# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
import radio
import random
from microbit import display, Image, button_a, sleep

# Анимация вспышка
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# Включить радиомодуль.
radio.on()

# Вечный цикл.
while True:
    # Если кнопка A нажата отправить сообщение.
    if button_a.was_pressed():
        radio.send('flash')
    # Читать входящие сообщения
    incoming = radio.receive()
    if incoming == 'flash':
        # Если пришло сообщение"flash" проиграть анимацию после случайно задержки
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        # Передать ответное сообщение.
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')
