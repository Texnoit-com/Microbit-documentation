Датчик Холла (магнитное поле)
-----------------------------

.. image:: Hall_Magnetic_Sensor.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Hall_Magnetic

Класс используется для определения объектов, имеющих поведение магнитного датчика
    
Пример объявления объекта::

    magnetic=Hall_Magnetic(pin0)

.. py:function:: magnetic.get_signal()

    Команда позволяет получить аналоговый сигнал с датчика

.. py:function:: magnetic.get_status(base_status:int, span=20)

    Команда возвращает **True**, если сигнал не вышел из диапазона (-span **base_status** +span)

Пример программы
****************

.. include:: sample.py
    :code: python