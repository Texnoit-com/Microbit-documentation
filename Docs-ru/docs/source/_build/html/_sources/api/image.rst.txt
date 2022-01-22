Изображение
***********


Класс ``Image`` используется для создания изображений, которые можно легко отобразить на
светодиодная матрица устройства. Учитывая объект изображения, его можно отобразить через
API отображения::

    display.show(Image.HAPPY)

.. image:: images/image-smile.png

Существует четыре способа создания образа:

- ``Image()`` - Создает пустое изображение 5x5

- ``Image(string)`` - Создает изображение, проанализировав строку.

- ``Image(width, height)`` - Создать пустое изображение заданного размера

- ``Image(width, height, buffer)`` - Создать изображение из заданного буфера


Класс
=======

.. py:class::
    Image(string)
    Image(width=None, height=None, buffer=None)

    Если используется ``string``, она должна состоять из цифр 0-9, расположенных в
    строки, описывающие изображение, например::

        image = Image("90009:"
                      "09090:"
                      "00900:"
                      "09090:"
                      "90009")

    создаст изображение размером 5×5. Конец строки обозначается двоеточием.
    Также можно использовать новую строку (\n) для обозначения конца строки. Пример::

        image = Image("90009\n"
                      "09090\n"
                      "00900\n"
                      "09090\n"
                      "90009")

    Другая форма создает пустое изображение со столбцами ``width`` и
    ``height`` строк. Опционально ``buffer`` может быть массивом
    ``width`` × ``height`` целые числа в диапазоне 0-9 для инициализации изображения::
   
        Image(2, 2, b'\x08\x08\x08\x08')

    или::

    	Image(2, 2, bytearray([9,9,9,9]))
	
    Создаст изображение размером 2 x 2 пикселя с максимальной яркостью..
    
    .. note::
    
        Аргументы ключевого слова не могут быть переданы ``buffer``.

    .. py:method:: width()

        Вернуть количество столбцов в изображении.


    .. py:method:: height()

        Вернуть количество строк в изображении.


    .. py:method:: set_pixel(x, y, value)

        Установите яркость пикселя в столбце «x» и строке «y» на
        ``value``, которое должно быть между 0 (темный) и 9 (яркий).

        Этот метод вызовет исключение при вызове любого из встроенных
        изображения только для чтения, такие как ``Image.HEART``.


    .. py:method:: get_pixel(x, y)

        Возвращает яркость пикселя в столбце ``x`` и строке ``y`` как
        целое число от 0 до 9.


    .. py:method:: shift_left(n)

        Вернуть новое изображение, созданное путем сдвига изображения влево на ``n``
        столбцы.


    .. py:method:: shift_right(n)

        Здвиг вправо ``image.shift_left(-n)``.

    .. py:method:: shift_up(n)

        вернуть новое изображение, созданное путем сдвига изображения вверх на ``n`` строк.


    .. py:method:: shift_down(n)

        Сдвиг вниз ``image.shift_up(-n)``.

    .. py:method:: crop(x, y, w, h)

        Верните новое изображение, обрезав изображение до ширины ``w`` и a
        высота ``h``, начиная с пикселя в столбце ``x`` и строке ``y``.

    .. py:method:: copy()

        Вернуть точную копию изображения.

    .. py:method:: invert()

        Верните новое изображение, инвертировав яркость пикселей в исходное изображение.

    .. py:method:: fill(value)

        Установите яркость всех пикселей изображения на
        ``value``, которое должно быть между 0 (темный) и 9 (яркий).

        Этот метод вызовет исключение при вызове любого из встроенных
        изображения только для чтения, такие как ``Image.HEART``.

    .. py:method:: blit(src, x, y, w, h, xdest=0, ydest=0)

        Скопируйте прямоугольник, определенный ``x``, ``y``, ``w``, ``h`` из изображения ``src`` в
        это изображение в ``xdest``, ``ydest``.
        Области в исходном прямоугольнике, но за пределами исходного изображения, обрабатываются 
        как имеющие значение 0. ``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()`` и ``crop()``
        все они могут быть реализованы с помощью ``blit()``.

        Например, img.crop(x, y, w, h) можно реализовать как::

            def crop(self, x, y, w, h):
                res = Image(w, h)
                res.blit(self, x, y, w, h)
                return res


Атрибуты
==========

Класс ``Image`` также имеет следующие встроенные экземпляры:
включены в качестве его атрибутов (имена атрибутов указывают, что изображение
представляет собой):

    * ``Image.HEART``
    * ``Image.HEART_SMALL``
    * ``Image.HAPPY``
    * ``Image.SMILE``
    * ``Image.SAD``
    * ``Image.CONFUSED``
    * ``Image.ANGRY``
    * ``Image.ASLEEP``
    * ``Image.SURPRISED``
    * ``Image.SILLY``
    * ``Image.FABULOUS``
    * ``Image.MEH``
    * ``Image.YES``
    * ``Image.NO``
    * ``Image.CLOCK12``, ``Image.CLOCK11``, ``Image.CLOCK10``, ``Image.CLOCK9``,
      ``Image.CLOCK8``, ``Image.CLOCK7``, ``Image.CLOCK6``, ``Image.CLOCK5``,
      ``Image.CLOCK4``, ``Image.CLOCK3``, ``Image.CLOCK2``, ``Image.CLOCK1``
    * ``Image.ARROW_N``, ``Image.ARROW_NE``, ``Image.ARROW_E``,
      ``Image.ARROW_SE``, ``Image.ARROW_S``, ``Image.ARROW_SW``,
      ``Image.ARROW_W``, ``Image.ARROW_NW``
    * ``Image.TRIANGLE``
    * ``Image.TRIANGLE_LEFT``
    * ``Image.CHESSBOARD``
    * ``Image.DIAMOND``
    * ``Image.DIAMOND_SMALL``
    * ``Image.SQUARE``
    * ``Image.SQUARE_SMALL``
    * ``Image.RABBIT``
    * ``Image.COW``
    * ``Image.MUSIC_CROTCHET``
    * ``Image.MUSIC_QUAVER``
    * ``Image.MUSIC_QUAVERS``
    * ``Image.PITCHFORK``
    * ``Image.XMAS``
    * ``Image.PACMAN``
    * ``Image.TARGET``
    * ``Image.TSHIRT``
    * ``Image.ROLLERSKATE``
    * ``Image.DUCK``
    * ``Image.HOUSE``
    * ``Image.TORTOISE``
    * ``Image.BUTTERFLY``
    * ``Image.STICKFIGURE``
    * ``Image.GHOST``
    * ``Image.SWORD``
    * ``Image.GIRAFFE``
    * ``Image.SKULL``
    * ``Image.UMBRELLA``
    * ``Image.SNAKE``

Наконец, связанные коллекции изображений были сгруппированы вместе::

    * ``Image.ALL_CLOCKS``
    * ``Image.ALL_ARROWS``


Команды
==========

.. code::

    repr(image)

Получить компактное строковое представление изображения.

.. code::

    str(image)

Получить удобочитаемое строковое представление изображения.

.. code::

    image1 + image2

Создайте новое изображение, добавив значения яркости из двух изображений для
каждый пиксель.

.. code::

    image * n

Создайте новое изображение, умножив яркость каждого пикселя на ``n``.
