Датчик Ультразвука
------------------

:download:`Скачать файл с классов <Ultrasonic.py>`

Ультразвуковой дальномер HC-SR04 – это помещенные на одну плату приемник и передатчик 
ультразвукового сигнала. Излучатель генерирует сигнал, который, отразившись от препятствия,
на приемник. Измерив время, за которое сигнал проходит до объекта и обратно, можно оценить
расстояние. Кроме самих приемника и передатчика, на плате находится еще и необходимая 
обвязка, чтобы сделать работу с этим датчиком простой и удобной.

.. image:: HC-SR04_Ultrasonic.png
    :width: 200px
    :align: center

Класс позволяет считывать расстояние от ультразвукового датчика HCSR04 или аналогичного.

Он использует внутреннее аппаратное устройство SPI для измерения длины возвращаемого эха, 
поэтому по умолчанию вы должны подключить контакт ``echo`` сонара к ``pin14`` micro:bit, 
а контакт ``Trig`` сонара к ``pin15`` micro:bit.

Датчик имеет один излучатель и приемник. Частота импульсов датчика около 10 микросекунд. 
Когда он получает сигнал от micro:bit, он посылает ультразвуковой сигнал через излучатель. 
Приемник улавливает отражение звука. Ширина импульса "эха" эквивалентна времени, 
которое требуется звуку, чтобы достичь объекта и вернуться. Это в  два раза больше, чем расстояние 
до объекта.

.. image:: spi1.png
    :width: 600px
    :align: center

Библиотека использует внутреннее аппаратное устройство spi для измерения "эха". 
SPI работает, используя один контакт для установки тактовой частоты с импульсами на требуемой частоте. 
Другой контакт используется для передачи битов в каждом тактовом цикле, а последний контакт 
используется для приема битов от другого устройства. Библиотека отправляет импульс через MOSI и 
ожидает получения чего-либо через MISO. Затем он измеряет длину возвращаемого импульса, 
считая эквивалентные «биты»

.. image:: spi2.png
    :width: 600px
    :align: center

Класс
*****

.. py:class::
    Ultrasonic

Класс используется для определения объектов, имеющих поведение ультразвукового датчика

.. code::

    sonar = Ultrasonic( trigger, echo, speed_sound)

Параметр **speed_sound** - скорость распространения звука при комнотной температуре. По умолчанию
показатель равен 343 000, Вы можете его корректировать:



.. py:function:: distance_mm()

    Возвращает расстояние до объекта в миллиметрах

.. py:exception:: distance_сm()

    Возвращает расстояние до объекта в сантиметрах

Пример программы
****************

.. include:: sample.py
    :code: python