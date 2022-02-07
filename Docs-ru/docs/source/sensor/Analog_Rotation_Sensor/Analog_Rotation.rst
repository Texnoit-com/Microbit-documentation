Переменный резистор
-------------------

:download:`Скачать файл с классов <Analog_Rotation.py>`

.. image:: Analog_Rotation_Sensor.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Analog_Rotation

Класс используется для определения объектов, имеющих поведение поворотного переменного резистора
    
Пример объявления объекта::

    rotation=Analog_Rotation(pin0)

.. py:function:: rotation.get_signal()

    Команда позволяет получить аналоговый сигнал

.. py:function:: rotation.get_angle(max_signal:int)

    Команда позволяет получить значение угла поворота в диапазоне 180.
    **max_signal** - максимальное аналоговое значение сигнала переменного резистора 

.. py:function:: rotation.get_scale(max_signal:int, scale:int)

    Команда позволяет получить значение угла поворота в диапазоне 180.
    **max_signal** - максимальное аналоговое значение сигнала переменного резистора 
    **scale** - размер диапазона.
     
Пример программы
****************

.. include:: sample.py
    :code: python