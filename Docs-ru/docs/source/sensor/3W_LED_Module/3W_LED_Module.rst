Сверхяркий светодиод
-----------------------


:download:`Скачать файл с классов <LED_3W_Module.py>`

.. image:: 3W_LED_Module.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    LED_3W_Module
    
Класс используется для определения объектов, имеющих поведение светодиода 
    
Пример объявления объекта::

    led=LED_3W_Module(pin1)

.. py:function:: led.on()

    Команда позволяет включить светодиод

.. py:function:: led.off()

    Команда позволяет выключить светодиод

.. py:function:: led.bright(arg:int)

    Команда включает светодиод с указанной яркостью (0-1023)

Пример программы
****************

.. include:: sample.py
    :code: python