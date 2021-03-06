Двухстрочный монитор 1602_I2C
-----------------------------

:download:`Скачать файл с классов <1602_I2C_Module.py>`

**I2C / IIC (Inter-Integrated Circuit)** – это протокол, изначально создававшийся для связи интегральных
микросхем внутри электронного устройства. Разработка принадлежит фирме Philips.

В основе i2c протокола является использование 8-битной шины, которая нужна для связи блоков в управляющей 
электронике, и системе адресации, благодаря которой можно общаться по одним и тем же проводам с 
несколькими устройствами.

.. image:: 1602_I2C_Module.png
    :width: 200px
    :align: center

- 16 знаков шириной, 2 ряда;
- Белый текст на синем фоне;
- Рабочее напряжение чипа: 4,5-5,5
- Оптимальное рабочее напряжение модуля 5,0 В.
- Включенная одиночная светодиодная подсветка легко регулируется с помощью резистора.
- Встроенный набор символов поддерживает английский текст
- Настройка потенциометром контраста
  
Класс
*****

.. py:class::
    1602_I2C

.. py:function:: ??()

Пример программы
****************

.. include:: sample.py
    :code: python