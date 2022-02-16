Датчик наклона
--------------

:download:`Скачать файл с классов <Digital_Tilt.py>`

.. image:: Digital_Tilt_Sensor.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Digital_Tilt

Класс используется для определения объектов, имеющих поведение датчика вибрации.
    
Пример объявления объекта::

    tilt= Digital_Tilt(pin0)

.. py:function:: tilt.vibration()

Команда возвращает **True**, если произошла вибрация датчика.

Пример программы
****************

.. include:: sample.py
    :code: python