Датчик температуры 18B20
------------------------

.. image:: 18B20_Temperature.png
    :width: 200px
    :align: center

Класс
*****

.. py:class::
    B20_Temperature

Класс используется для определения объектов, имеющих поведение аналогового датчика температуры
    
Пример объявления объекта::

    temp=Analog_Temperature(pin0)

.. py:function:: temp.get_signal()

Команда позволяет получить аналоговый сигнал с датчика

.. py:function:: temp.temperature()

Команда позволяет получить сигнал с датчика и переводит его в градусы

Пример программы
****************

.. include:: sample.py
    :code: python