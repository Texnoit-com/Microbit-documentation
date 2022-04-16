Датчик температуры (аналоговый)
-------------------------------

:download:`Скачать файл с классов <Analog_Temperature.py>`

.. image:: Analog_Temperature_Sensor.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Analog_Temperature

Класс используется для определения объектов, имеющих поведение аналогового датчика температуры
    
Пример объявления объекта::

    temp=Analog_Temperature(pin0)

.. py:function:: temp.get_signal()

Команда позволяет получить аналоговый сигнал с датчика

Пример программы
****************

.. include:: sample.py
    :code: python