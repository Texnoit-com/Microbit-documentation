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

Контакты обеспечивают цифровые и аналоговые функции ввода/вывода сигналов. Запомните, что некоторые 
контакты используются во внутреннем функционале платы (дисплей, кнопки и т. д.). При их использовании
необходимо отключать внутренний функционал.

Каждый контакт предоставляется как объект непосредственно в модуле ``microbit``. Этот
делает API относительно простым:

    * pin0
    * pin1
    * ...
    * pin15
    * pin16
    * *Предупреждение: P17-P18 (включительно) недоступны.*
    * pin19
    * pin20
    * pin_logo **V2**
    * pin_speaker **V2**

Каждый контакт является экземпляром класса ``MicroBitPin``, который предлагает следующий API::

    # Отправляет цифровой сигнал (может быть 0, 1, False, True)

    pin.write_digital(value)

    # Возвращает цифровой сигнал 1 или 0

    pin.read_digital()

    # Отправляет аналоговый сигнал от 0 до 1023

    pin.write_analog(value)

    # Возвращает аналоговый сигнал от 0 до 1023

    pin.read_analog()

    # устанавливает период ШИМ-вывода/вывода в миллисекундах
    # (подробнее https://en.wikipedia.org/wiki/Pulse-width_modulation)

    pin.set_analog_period(int)

    # устанавливает период ШИМ-вывода/вывода в микросекундах
    # (подробнее https://en.wikipedia.org/wiki/Pulse-width_modulation)

    pin.set_analog_period_microseconds(int)

    # Доступно только для сенсорных контактов 0, 1 и 2. Возвращает логическое значение, если контакт затронуть

    pin.is_touched()

    # Доступно только для сенсорных контактов 0, 1, 2, а также для логотипа micro:bit V2.
    # Устанавливает сенсорный режим. Значение может быть либо RESISTIVE, либо CAPACITIVE.

    pin.set_touch_mode(value)

За исключением контактов, отмеченных **V2**, которые предлагают следующий API::
    
    pin_logo
    
    # возвращает логическое значение если тронуть логотип

    pin_logo.is_touched()

    # Устанавливает сенсорный режим. Значение может быть либо RESISTIVE, либо CAPACITIVE

    pin.set_touch_mode(value)

pin_speaker:
    
Принадлежит классу ``MicroBitPin``, но не имеет функции ``pin.is_touched()``.

Изображение
-----------

.. note::

    Вам не всегда нужно создавать изображение самостоятельно — Вы можете получить доступ к
    изображениям, непосредственно с помощью `display.image`. `display.image`
    это экземпляр `Image`, поэтому Вы можете использовать одинаковые методы.

Изображение API::

    # создает пустое изображение 5x5

    image = Image()

    # создать изображение из строки - каждый символ в строке представляет собой
    # уровень яркости светодиода - 0 выключен, 9 - максимальная яркость. Двоеточие ":"
    # указывает на конец строки.

    image = Image('90009:09090:00900:09090:90009:')

    # создать пустое изображение заданного размера

    image = Image(width, height)

    # Возвращает ширину изображения

    image.width()

    # Возвращает высоту изображения

    image.height()

    # Управляет яркостью светодиода в указанной позиции ( от 0 до 5).
    # value от 0 до 9

    image.set_pixel(x, y, value)

    # Возвращает яркость пикселя в указанной позиции (от 0 до 9)

    image.get_pixel(x, y)

    # возвращает новое изображение, созданное сдвигом изображения влево на 'n' раз.

    image.shift_left(n)

    # возвращает новое изображение, созданное сдвигом изображения вправо на 'n' раз.

    image.shift_right(n)

    # возвращает новое изображение, созданное сдвигом изображения вверх на 'n' раз.

    image.shift_up(n)

    # возвращает новое изображение, созданное сдвигом изображения вниз на 'n' раз.

    image.shift_down(n)

    # получить компактное строковое представление изображения

    repr(image)

    # получить строковое представление изображения

    str(image)

    #operators
    # возвращает новое изображение, созданное путем наложения двух изображений

    image + image

    # возвращает новое изображение, созданное путем умножения яркости каждого пикселя на n

    image * n

**Изображения из библиотеки**

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

Время:

``Image.CLOCK1`` ``Image.CLOCK2`` ``Image.CLOCK3`` ``Image.CLOCK4``
``Image.CLOCK5`` ``Image.CLOCK6`` ``Image.CLOCK7`` ``Image.CLOCK8``
``Image.CLOCK9`` ``Image.CLOCK10`` ``Image.CLOCK11`` ``Image.CLOCK12``

Стороны света:

``Image.ARROW_N`` ``Image.ARROW_NE`` ``Image.ARROW_E`` ``Image.ARROW_SE``
``Image.ARROW_S`` ``Image.ARROW_SW`` ``Image.ARROW_W`` ``Image.ARROW_NW``

Ниже приведены название списков изображений Python. Вы можете их обрабатывать как списки.

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
---------------------

Динамик включен по умолчанию, и к нему можно получить доступ с помощью объекта ``speaker``. Это
можно отключить или включить::

    # отключить встроенный динамик

    speaker.off()

    # включить встроенный динамик

    speaker.on()

    # возвращает True или False, чтобы указать, включен или выключен динамик

    speaker.is_on()


Протокол UART
-------------

Используйте ``uart`` для связи с последовательным устройством, подключенным к контактам ввода-вывода устройства::

    # Настроки связи  (используйте контакты 0 [TX] и 1 [RX]) со скоростью 9600.

    uart.init()

    # Возвращает True или False, проверяя есть ли входящие символы на чтение.

    uart.any()

    # Прочитать n входящих символов.

    uart.read(n)

    # Прочитать как можно больше входящих данных.

    uart.read()

    # Вернуть все символы до символа новой строки.

    uart.readline()

    # Читать байты в указанный буфер.

    uart.readinto(buffer)

    # Записать байты из буфера на подключенное устройство.

    uart.write(buffer)
