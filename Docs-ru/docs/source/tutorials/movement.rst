Акселерометр
------------

В микроконтроллере Microbit встроен датчик - акселерометр. Он измеряет движение вдоль осей:

* X - наклон влево и вправо.
* Y - наклоны вперед и назад.
* Z - движение вверх и вниз.

Для каждой оси есть метод, который возвращает положительное или отрицательное число.
Единица измерения акселерометра мм/с. Акселерометр может фиксировать: вибрации, 
рывки, наклонное положение, столкновения и движение объекта.

Например измерение отклонений по оси **X** и отображения буквы ``R`` - отклонение вправо, 
``L`` - отклонение на лево::

    from microbit import *

    while True:
        reading = accelerometer.get_x()
        if reading > 20:
            display.show("R")
        elif reading < -20:
            display.show("L")
        else:
            display.show("-")

В строке ``reading = accelerometer.get_x()`` записана переменная, которая хранит 
значение функции считывания отклонения по оси ``X``.Далее прописано условие реагирование 
на события отклонения вправо и влено на 20.

Для отслеживания отклонений по другим осям используйте функции``get_y`` по оси ``Y`` 
и  ``get_z`` по оси ``Z``.

Современные устройства тоже содержат датчик акселерометр: телефоны, планшеты, электронные книги,
игровые устройства и т. д.

Музыкальный инструмент
++++++++++++++++++++++

Давайте создадим устройство, которое проигрывает звук, который зависит от отклонения по оси ``Y``.
Отклонение меняет воспроизводимую частоту.

Подключите динамик к микроконтроллеру, если у Вас версия ``V1``.

.. image:: pin0-gnd.png

Напишите программный код::

    from microbit import *
    import music

    while True:
        music.pitch(accelerometer.get_y(), 10)

Продолжительность проигрывание очень быстрая 10 милисекунд.