Джойстик
--------

:download:`Скачать файл с классов <Joystick.py>`

.. image:: Joystick_Module.png
    :width: 100px
    :align: center

Аналоговый джойстик чувствителен к тому, насколько далеко Вы перемещаете стик в любом 
конкретном направлении. Направление влево/вправо называют горизонтальной осью (осью X). 
Направление вверх/вниз называют вертикальной осью (осью Y). 

При нажатии на стик происходит события нажатия на кнопку, сигнал можно снять с цифрового контакта **SW**.


Класс
*****

.. py:class::
    Joystick

Класс используется для определения объектов, имеющих поведение джойстика.
    
Пример объявления объекта::

    joys=Joystick(pin0, pin1, pin2)

.. py:function:: joys.get_x()

    Команда возвращает показание по оси X.

.. py:function:: joys.get_y()

    Команда возвращает показание по оси Y.

.. py:function:: joys.click()

    Команда возвращает сигнал нажатия на кнопку.

.. py:function:: joys.play_cross()

    Команда возвращает сигналы **UP**, **Down**, **Left**, **Right**, **0**. 
    Принцип работы цифрового джойстика.

.. py:function:: joys.play_diagonal()

    Команда возвращает сигналы **Up**, **Down**, **Left**, **Right**, **0**.
    Диаганальные сигналы **Up-Left**, **Up-Right**, **Down-Left**, **Down-Right**.
    Принцип работы цифрового джойстика.


Пример программы
****************

.. include:: sample.py
    :code: python