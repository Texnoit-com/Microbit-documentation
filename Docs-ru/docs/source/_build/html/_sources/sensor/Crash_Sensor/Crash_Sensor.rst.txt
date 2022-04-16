Кнопка (концевик)
-----------------

:download:`Скачать файл с классов <Crash_Sensor.py>`

.. image:: Crash_Sensor.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Crash_Sensor

Класс используется для определения объектов, имеющих поведение кнопки-концевик 
    
Пример объявления объекта::

    crash=Crash_Sensor(pin0)

.. py:function:: crash.is_pressed()

    Команда возвращает **True**, если кнопки-концевик нажата

.. py:function:: crash.click(time:int)

    Команда возвращает **True**, если кнопки-концевик была нажата-отжата ("клик")
    **time** - указывает паузу между состояниями нажата-отжата

.. py:function:: crash.count_pressed()

    Команда возвращает количество прошедших ее опросов методом **is_pressed()**,
    при которых кнопки-концевик была нажата

.. py:function:: crash.reset_pressed()

    Команда сбрасывает счетчик нажатий
    
Пример программы
****************

.. include:: sample.py
    :code: python