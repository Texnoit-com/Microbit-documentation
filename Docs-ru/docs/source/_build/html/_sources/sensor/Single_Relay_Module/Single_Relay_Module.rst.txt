Реле
----

:download:`Скачать файл с классов <Single_Relay.py>`

.. image:: Single_Relay_Module.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Single_Relay

Класс используется для определения объектов, имеющих поведение реле 
    
Пример объявления объекта::

    relay=LED_Module(pin1)

.. py:function:: relay.on()

    Команда позволяет включить светодиод

.. py:function:: relay.off()

    Команда позволяет выключить светодиод

Пример программы
****************

.. include:: sample.py
    :code: python