..
   MicroPython license information
   ===============================

   The MIT License (MIT)

   Copyright (c) 2013-2017 Damien P. George, and others

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.


utime (модуль работы со временем)
*********************************

.. py:module:: utime

Модуль ``utime`` предоставляет функции для получения текущего времени и даты,
измерения временных интервалов и задержек.

.. note::
    Модуль ``utime`` представляет собой реализацию MicroPython стандартного модуля Python.
    модуль ``time``. Его можно импортировать как с помощью ``import utime``, так и с помощью
    ``import time``, но модуль тот же.


Функции
=========

.. method:: utime.sleep(seconds)

    Задержка в течение заданного количества секунд. Вы можете использовать число с плавающей запятой
    заснуть на долю секунды или использовать 
    
    :func:`utime.sleep_ms()` и :func:`utime.sleep_us()`.


.. method:: utime.sleep_ms(ms)

    Задержка для заданного количества миллисекунд должна быть положительной или равной 0.


.. method:: utime.sleep_us(us)

    Задержка для заданного количества микросекунд должна быть положительной или равной 0.


.. method:: utime.ticks_ms()

    Возвращает увеличивающийся счетчик миллисекунд с произвольной контрольной точкой.


.. method:: utime.ticks_us()

    Так же, как :func:`utime.ticks_ms()` выше, но в микросекундах.


.. method:: utime.ticks_add(ticks, delta)

    Смещение значения тиков на заданное число, которое может быть как положительным, так и
    отрицательный. Учитывая значение тиков, эта функция позволяет вычислить тики
    значение дельта тикает до или после него, следуя модульной арифметике
    определение тиковых значений.

    Example:

    .. code-block:: python

        # Узнать какое значение тиков было 100 мс назад
        print(ticks_add(time.ticks_ms(), -100))

        # Рассчитать срок эксплуатации и протестировать его
        deadline = ticks_add(time.ticks_ms(), 200)
        while ticks_diff(deadline, time.ticks_ms()) > 0:
            do_a_little_of_something()

        # Узнайте TICKS_MAX, используемый этим портом
        print(ticks_add(0, -1))


.. method:: utime.ticks_diff(ticks1, ticks2)

    Измерьте разницу в отметках между значениями, возвращенными из
    :func:`utime.ticks_ms()` или :func:`ticks_us()`.

    Порядок аргументов такой же, как и для вычитания пользователем,
    ``ticks_diff(ticks1, ticks2)`` имеет то же значение, что и ``ticks1 - ticks2``.

    :func:`utime.ticks_diff()` предназначен для различных видов использования
    разницы, среди них:

    Опрос с тайм-аутом. В этом случае порядок событий известен, и вы
    будете иметь дело только с положительными результатами :func:`utime.ticks_diff()`:

    .. code-block:: python

        # Дождитесь подтверждения вывода GPIO, но не более 500 мкс.
        start = time.ticks_us()
        while pin.value() == 0:
            if time.ticks_diff(time.ticks_us(), start) > 500:
                raise TimeoutError


    Планирование событий. В этом случае результат :func:`utime.ticks_diff()` может быть
    отрицательный, если событие просрочено:


    .. code-block:: python

        # Этот фрагмент кода не оптимизирован
        now = time.ticks_ms()
        scheduled_time = task.scheduled_time()
        if ticks_diff(scheduled_time, now) > 0:
            print("Too early, let's nap")
            sleep_ms(ticks_diff(scheduled_time, now))
            task.run()
        elif ticks_diff(scheduled_time, now) == 0:
            print("Right at time!")
            task.run()
        elif ticks_diff(scheduled_time, now) < 0:
            print("Oops, running late, tell task to run faster!")
            task.run(run_faster=true)