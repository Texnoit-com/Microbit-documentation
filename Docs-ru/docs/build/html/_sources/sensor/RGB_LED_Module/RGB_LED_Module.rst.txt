Модуль светодиода RGB
------------------------

:download:`Скачать файл с классов <RGB_LED_Module.py>`

.. image:: RGB_LED_Module.png
    :width: 200px
    :align: center

Класс
*****

.. py:class::
    RGB_LED_Module

Класс используется для определения объектов, имеющих поведение светодиода-RGB
    
Пример объявления объекта::

    led=RGB_LED_Module(red=pin0, green=pin1, blue=pin2)

.. py:function:: led.on_red()

    Команда позволяет включить красный свет светодиода. 
    Аналогичные команды **on_green()** и **on_blue()**.

.. py:function:: led.off_red()

    Команда позволяет выключить красный свет светодиода.
    Аналогичные команды **off_green()** и **off_blue()**.

.. py:function:: led.bright_red(arg:int)

    Команда позволяет включить красный свет с указанной яркостьюсветодиода.
    Аналогичные команды **bright_green(arg:int)** и **bright_blue(arg:int)**.

.. py:function:: led.off()

    Команда позволяет выключить светодиод полностью

.. py:function:: led.conversion(start=led.red, finish=led.green, time=3000)

    Команда позволяет сделать планый переход от одного цвета к другому (от красного к зеленому) за указанное время (мм).

.. py:function:: random_rgb(time=3000, step=10)

    Команда выводит случайные цвета светодиода с шагом step в течении указанного времени time


Пример программы
****************

.. include:: sample.py
    :code: python