Модуль Microbit
***************

.. py:module:: microbit


Доступ до всех функций осуществляется через ``microbit``.


Функции
=======

.. py:function:: panic(n)

   Формирование ошибки и передача номера ошибки. Для продолжения работы требуется перезагрузка Microbit::

        microbit.panic(255)


.. py:function:: reset()

    Перезагрузка платы::

        microbit.reset()

.. py:function:: sleep(n)

    Задержка ``n`` миллисекунд. Приостановка работы Microbit::

        microbit.sleep(1000)

.. py:function:: running_time()

   Возвращает количество миллисекунд с момента включения платы или перезапущен::

       microbit.running_time()

.. py:function:: temperature()

    Возвращает температуру Microbit в градусах Цельсия::

        microbit.temperature()

Атрибуты
========

.. toctree::
    :maxdepth: 1

    button.rst
    pin.rst


Класс
=======

.. toctree::
    :maxdepth: 1

    image.rst
    Sound <audio.rst>


Модули
=======

.. toctree::
    :maxdepth: 1

    accelerometer.rst
    Audio V2 <audio.rst>
    compass.rst
    display.rst
    i2c.rst
    microphone.rst
    speaker.rst
    spi.rst
    uart.rst
