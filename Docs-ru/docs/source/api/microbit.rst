Microbit Module
***************

.. py:module:: microbit


The ``microbit`` module gives you access to all the hardware that is built-in
into your board.


Функции
=========

.. py:function:: panic(n)

    Enter a panic mode. Requires restart. Pass in an arbitrary integer <= 255
    to indicate a status::

        microbit.panic(255)


.. py:function:: reset()

    Restart the board.


.. py:function:: sleep(n)

    Wait for ``n`` milliseconds. One second is 1000 milliseconds, so::

        microbit.sleep(1000)

    will pause the execution for one second.  ``n`` can be an integer or
    a floating point number.


.. py:function:: running_time()

    Return the number of milliseconds since the board was switched on or
    restarted.


.. py:function:: temperature()

    Return the temperature of the micro:bit in degrees Celcius.


Атрибуты
==========

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