Microbit Micropython API
*************************

Модуль
======

Весь функционал расположен в библиотеке::

    from microbit import *

В дальнейщем в коде это строка указываться не будет. Вы ее подключаете самостоятельно

Функции доступные на прямую::

    # Задержка, указывается в миллисекундах.
    sleep(ms)
    # возвращает количество миллисекунд с момента последнего включения Microbit.
    running_time()
    # Переводит Microbit в режим ошибки выполнения.
    panic(error_code)
    # Перезагрузка Microbit.
    reset()
    # Устанавливает громкость динамиков.
    set_volume(128)    # V2

Остальная функциональность обеспечивается объектами и классами в модуле микробит, как будет описано ниже.

Обратите внимание, что API предоставляет только целые числа (т. е. числа с плавающей запятой не нужны, 
но они могут быть приняты). Таким образом, мы используем миллисекунды в качестве стандартной единицы времени.

.. note::
    Вы можете увидеть список всех доступных модулей, написав ``help('modules')`` в REPL.

Кнопки
-------

На микробите встроены 2 кнопки::

    button_a
    button_b

Объеккты имеют методы::

    # возвращает True или False,обозначая была ли кнопка нажата во время вызов метода.
    button.is_pressed()
    # возвращает True или False, чтобы указать, была ли кнопка нажата после последнего вызова этой метода
    button.was_pressed()
    # возвращает общее количество нажатий на кнопоку и сбрасывает этот счетчик на ноль
    button.get_presses()

Дисплей
-------

Светодиодный дисплей выводится через объект `display`::

    # Возвращает значения яркости пикселя ( от 0 до 9) по координатам x, y.
    display.get_pixel(x, y)
    # Устанавливает значения яркости пикселя ( от 0 до 9) по координатам x, y.
    display.set_pixel(x, y, val)
    # Очищает дисплей.
    display.clear()
    # Выводит изображение на дисплей.
    display.show(image, delay=0, wait=True, loop=False, clear=False)
    # Может выводить итерируемый объект с задержкой.
    display.show(iterable, delay=400, wait=True, loop=False, clear=False)
    # Бегущая строка.
    display.scroll(string, delay=400)

Звук **V2**
-----------------
Команды описывающие работу со звуком::

    # Переключение режима работы (тихо, громко).
    SoundEvent.LOUD = SoundEvent('loud')
    # Переключение в режим повышенных шумов.
    SoundEvent.QUIET = SoundEvent('quiet')

Микрофон **V2**
-----------------

Доступ к микрофону осуществляется через объект `microphone`::

    # Возвращает имя последнего записанного звукового события

    current_event()

    # Отследить изменение событий `SoundEvent.LOUD`и `SoundEvent.QUIET`. 
    # Возвращает true, если звук был слышен хотя бы один раз с момента последнего
    # вызов, иначе `false`

    was_event(event)

    # Кортеж историй звуковых событий

    get_events()

    #Установка порогового уровня реагирования на звук в диапазоне 0-255. Например,
    # `set_threshold(SoundEvent.LOUD, 250)` сработает, только если
    # звук очень громкий (>= 250).

    set_threshold(128)

    # Возвращает представление уровня звукового давления в диапазоне от 0 до 255.

    sound_level()

Контакты
--------

Provide digital and analog input and output functionality, for the pins in the
connector, the **V2** logo and the **V2** speaker. Some pins are connected
internally to the I/O that drives the LED matrix and the buttons.

Each pin is provided as an object directly in the ``microbit`` module.  This
keeps the API relatively flat, making it very easy to use:

    * pin0
    * pin1
    * ...
    * pin15
    * pin16
    * *Warning: P17-P18 (inclusive) are unavailable.*
    * pin19
    * pin20
    * pin_logo **V2**
    * pin_speaker **V2**

Each of these pins are instances of the ``MicroBitPin`` class, which offers the following API::

    # value can be 0, 1, False, True
    pin.write_digital(value)
    # returns either 1 or 0
    pin.read_digital()
    # value is between 0 and 1023
    pin.write_analog(value)
    # returns an integer between 0 and 1023
    pin.read_analog()
    # sets the period of the PWM output of the pin in milliseconds
    # (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
    pin.set_analog_period(int)
    # sets the period of the PWM output of the pin in microseconds
    # (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
    pin.set_analog_period_microseconds(int)
    # Only available for touch pins 0, 1, and 2. Returns boolean if the pin
    # is touched
    pin.is_touched()
    # Only available for touch pins 0, 1, 2 and on micro:bit V2 also the logo.
    # Sets the touch mode. Value can be either RESISTIVE or CAPACITIVE
    pin.set_touch_mode(value)

Except in the case of the pins marked **V2**, which offers the following API::
    
pin_logo::

    # returns boolean for logo touch pin
    pin_logo.is_touched()
    # Sets the touch mode. Value can be either RESISTIVE or CAPACITIVE
    pin.set_touch_mode(value)

pin_speaker:
    
As above ``MicroBitPin`` class, but does not include ``pin.is_touched()``.

Изображение
-----------

.. note::

    You don't always need to create one of these yourself - you can access the
    image shown on the display directly with `display.image`. `display.image`
    is just an instance of `Image`, so you can use all of the same methods.

Images API::

    # creates an empty 5x5 image
    image = Image()
    # create an image from a string - each character in the string represents an
    # LED - 0 (or space) is off and 9 is maximum brightness. The colon ":"
    # indicates the end of a line.
    image = Image('90009:09090:00900:09090:90009:')
    # create an empty image of given size
    image = Image(width, height)
    # initialises an Image with the specified width and height. The buffer
    # should be an array of length width * height
    image = Image(width, height, buffer)

    # methods
    # returns the image's width (most often 5)
    image.width()
    # returns the image's height (most often 5)
    image.height()
    # sets the pixel at the specified position (between 0 and 9). May fail for
    # constant images.
    image.set_pixel(x, y, value)
    # gets the pixel at the specified position (between 0 and 9)
    image.get_pixel(x, y)
    # returns a new image created by shifting the picture left 'n' times.
    image.shift_left(n)
    # returns a new image created by shifting the picture right 'n' times.
    image.shift_right(n)
    # returns a new image created by shifting the picture up 'n' times.
    image.shift_up(n)
    # returns a new image created by shifting the picture down 'n' times.
    image.shift_down(n)
    # get a compact string representation of the image
    repr(image)
    # get a more readable string representation of the image
    str(image)

    #operators
    # returns a new image created by superimposing the two images
    image + image
    # returns a new image created by multiplying the brightness of each pixel by n
    image * n

**Built-in images**

``Image.HEART``
``Image.HEART_SMALL``
``Image.HAPPY``
``Image.SMILE``
``Image.SAD``
``Image.CONFUSED``
``Image.ANGRY``
``Image.ASLEEP``
``Image.SURPRISED``
``Image.SILLY``
``Image.FABULOUS``
``Image.MEH``
``Image.YES``
``Image.NO``
``Image.TRIANGLE``
``Image.TRIANGLE_LEFT``
``Image.CHESSBOARD``
``Image.DIAMOND``
``Image.DIAMOND_SMALL``
``Image.SQUARE``
``Image.SQUARE_SMALL``
``Image.RABBIT``
``Image.COW``
``Image.MUSIC_CROTCHET``
``Image.MUSIC_QUAVER``
``Image.MUSIC_QUAVERS``
``Image.PITCHFORK``
``Image.XMAS``
``Image.PACMAN``
``Image.TARGET``
``Image.TSHIRT``
``Image.ROLLERSKATE``
``Image.DUCK``
``Image.HOUSE``
``Image.TORTOISE``
``Image.BUTTERFLY``
``Image.STICKFIGURE``
``Image.GHOST``
``Image.SWORD``
``Image.GIRAFFE``
``Image.SKULL``
``Image.UMBRELLA``
``Image.SNAKE``

Clock:

``Image.CLOCK1`` ``Image.CLOCK2`` ``Image.CLOCK3`` ``Image.CLOCK4``
``Image.CLOCK5`` ``Image.CLOCK6`` ``Image.CLOCK7`` ``Image.CLOCK8``
``Image.CLOCK9`` ``Image.CLOCK10`` ``Image.CLOCK11`` ``Image.CLOCK12``

Arrows:

``Image.ARROW_N`` ``Image.ARROW_NE`` ``Image.ARROW_E`` ``Image.ARROW_SE``
``Image.ARROW_S`` ``Image.ARROW_SW`` ``Image.ARROW_W`` ``Image.ARROW_NW``

The following are Python lists of images, useful for automatically displaying an
animation or manually iterating through them.

``Image.ALL_CLOCKS``
``Image.ALL_ARROWS``

Акселерометр
-------------

The accelerometer is accessed via the ``accelerometer`` object::

    # read the X axis of the device. Measured in milli-g.
    accelerometer.get_x()
    # read the Y axis of the device. Measured in milli-g.
    accelerometer.get_y()
    # read the Z axis of the device. Measured in milli-g.
    accelerometer.get_z()
    # get tuple of all three X, Y and Z readings (listed in that order).
    accelerometer.get_values()
    # return the name of the current gesture.
    accelerometer.current_gesture()
    # return True or False to indicate if the named gesture is currently active.
    accelerometer.is_gesture(name)
    # return True or False to indicate if the named gesture was active since the
    # last call.
    accelerometer.was_gesture(name)
    # return a tuple of the gesture history. The most recent is listed last.
    accelerometer.get_gestures()

The recognised gestures are: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``, ``8g``, ``shake``.


Компас
-------

The compass is accessed via the `compass` object::

    # calibrate the compass (this is needed to get accurate readings).
    compass.calibrate()
    # return a numeric indication of degrees offset from "north".
    compass.heading()
    # return an numeric indication of the strength of magnetic field around
    # the micro:bit.
    compass.get_field_strength()
    # returns True or False to indicate if the compass is calibrated.
    compass.is_calibrated()
    # resets the compass to a pre-calibration state.
    compass.clear_calibration()

Протокол I2C
------------

There is an I2C bus on the micro:bit that is exposed via the `i2c` object.  It has the following methods::

    # read n bytes from device with addr; repeat=True means a stop bit won't
    # be sent.
    i2c.read(addr, n, repeat=False)
    # write buf to device with addr; repeat=True means a stop bit won't be sent.
    i2c.write(addr, buf, repeat=False)

Звук **V2**
------------

A set of expressive sounds are available to the micro:bit **V2**. They can be
accessed via the ``microbit`` module and played with the :doc:`audio <audio>` module.

**Built-in sounds**

``Sound.GIGGLE``
``Sound.HAPPY``
``Sound.HELLO``
``Sound.MYSTERIOUS``
``Sound.SAD``
``Sound.SLIDE``
``Sound.SOARING``
``Sound.SPRING``
``Sound.TWINKLE``
``Sound.YAWN``

Генератор речи **V2**
--------------

The speaker is enabled by default and can be accessed using the ``speaker`` object. It
can be turned off or on::

    # disable the built-in speaker
    speaker.off()
    # enable the built-in speaker
    speaker.on()
    # returns True or False to indicate if the speaker is on or off
    speaker.is_on()


Протокол UART
-------------

Use ``uart`` to communicate with a serial device connected to the device's I/O pins::

    # set up communication (use pins 0 [TX] and 1 [RX]) with a baud rate of 9600.
    uart.init()
    # return True or False to indicate if there are incoming characters waiting to
    # be read.
    uart.any()
    # return (read) n incoming characters.
    uart.read(n)
    # return (read) as much incoming data as possible.
    uart.read()
    # return (read) all the characters to a newline character is reached.
    uart.readline()
    # read bytes into the referenced buffer.
    uart.readinto(buffer)
    # write bytes from the buffer to the connected device.
    uart.write(buffer)
