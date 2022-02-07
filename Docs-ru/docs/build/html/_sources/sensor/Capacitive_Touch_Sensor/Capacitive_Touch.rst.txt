Емкостной датчик
----------------

.. image:: Capacitive_Touch_Sensor.png
    :width: 100px
    :align: center

Класс
*****

:download:`Скачать файл с классов <Capacitive_Touch.py>`

.. py:class::
    Capacitive_Touch

Класс используется для определения объектов, имеющих поведение емкостного датчика
    
Пример объявления объекта::

    touch=Push_Button(pin0)

.. py:function:: touch.is_pressed()

    Команда возвращает **True**, если прилодижить палец к емкостному датчику

.. py:function:: touch.click(time:int)

    Команда возвращает **True**, если было прикосновение к емкостному датчику. 
    **time** - указывает паузу между состояниями прикосновния и базовым

.. py:function:: touch.count_pressed()

    Команда возвращает количество прошедших ее опросов методом **is_pressed()**,
    при которых было прикосновение к емкостному датчику

.. py:function:: touch.reset_pressed()

    Команда сбрасывает счетчик прикосновений

Пример программы
****************

.. include:: sample.py
    :code: python