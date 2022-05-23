"""
    Повторно отображает случайные цвета на светодиодной ленте.
"""
from random import randint

import neopixel
from microbit import pin0, sleep

# Установите длину ленты
np = neopixel.NeoPixel(pin0, 8)

while True:
    # Включение ленты
    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)
        # Назначьте текущему светодиоду случайное значение красного, зеленого и синего цветов от 0 до 60
        np[pixel_id] = (red, green, blue)
        # Отображение светодиодов
        np.show()
        sleep(100)
