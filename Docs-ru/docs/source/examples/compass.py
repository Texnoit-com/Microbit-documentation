"""
    compass.py
    Создает компас.
    Сначала пользователю необходимо откалибровать компас. В компасе используется
    встроенные изображения часов для отображения положения стрелки
"""
from microbit import Image, compass, display, sleep

# Начало калибровки
compass.calibrate()

while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
