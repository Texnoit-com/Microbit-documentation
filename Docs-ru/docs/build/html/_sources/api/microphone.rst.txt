Микрофон **V2**
*****************

.. py:module:: microbit.microphone

Этот объект позволяет вам получить доступ к встроенному микрофону, доступному на
микро:бит **V2**. Его можно использовать для реакции на звук. Вход микрофона
расположен на передней панели рядом со светодиодом активности микрофона,
который горит, когда микрофон используется.

.. image:: microphone.png
    :width: 300px
    :align: center
    :height: 240px
    :alt: micro:bit with microphone LED on

События микрофона
=================

Микрофон может реагировать на предопределенный набор звуковых событий, которые
в зависимости от амплитуды и длины волны звука.

Эти звуковые события представлены экземплярами класса SoundEvent,
доступны через переменные в ``microbit.SoundEvent``:

- ``microbit.SoundEvent.QUIET``: Представляет переход звуковых событий,
  от ``loud`` до ``quiet`` как разговор или фоновая музыка.

- ``microbit.SoundEvent.LOUD``: Представляет переход звуковых событий,
  от ``quiet`` до ``loud`` например, аплодисментов или криков.

Функции
========

.. py:function:: current_event()

    * **return**: название последнего записанного звукового события,
      ``SoundEvent('loud')`` или ``SoundEvent('quiet')``.

.. py:function:: was_event(event)

    * **event**: звуковое событие, например ``SoundEvent.LOUD`` или
      ``SoundEvent.QUIET``.

    * **return**: ``true`` если звук был слышен хотя бы один раз с момента последнего
      позвони, иначе ``false``. ``was_event()`` также очищает звук
      история событий перед возвратом.

.. py:function:: is_event(event)

    * **event**: звуковое событие, например ``SoundEvent.LOUD`` или
      ``SoundEvent.QUIET``.
    * **return**: ``true`` если звуковое событие является последним с момента последнего
      позвони, иначе ``false``. Не очищает историю звуковых событий.

.. py:function:: get_events()

    * **return**: кортеж истории событий. Самый последний указан последним.
      ``get_events()`` также очищает историю звуковых событий перед возвратом.

.. py:function:: set_threshold(event, value)

    * **event**: звуковое событие, например ``SoundEvent.LOUD`` или
      ``SoundEvent.QUIET``.
    
    * **value**: Пороговый уровень в диапазоне 0-255. Например,
      ``set_threshold(SoundEvent.LOUD, 250)`` будет срабатывать только в том случае, если звук
      очень громко (>= 250).

.. py:function:: sound_level()

    * **return**: представление уровня звукового давления в диапазоне от 0 до 255.


Примеры
=======

Пример, запускающий некоторые функции микрофона:

    # Базовый тест для микрофона. Этот тест должен обновлять дисплей, когда
    # Нажата кнопка A и *pressed* громкий или тихий звук, распечатывая
    # Результаты. На кнопке B этот тест должен обновлять дисплей при громком или
    # тихий звук *is* слышен, вывод результатов. При встряхивании это должно печатать
    # последние слышимые звуки, вы должны попробовать этот тест, издавая громкий звук
    # и тихий, прежде чем встряхнуть.

Код::

    from microbit import *

    display.clear()
    sound = microphone.current_event()

    while True:
        if button_a.is_pressed():
            if microphone.current_event() == SoundEvent.LOUD:
                display.show(Image.SQUARE)
                uart.write('isLoud\n')
            elif microphone.current_event() == SoundEvent.QUIET:
                display.show(Image.SQUARE_SMALL)
                uart.write('isQuiet\n')
            sleep(500)
        display.clear()
        if button_b.is_pressed():
            if microphone.was_event(SoundEvent.LOUD):
                display.show(Image.SQUARE)
                uart.write('wasLoud\n')
            elif microphone.was_event(SoundEvent.QUIET):
                display.show(Image.SQUARE_SMALL)
                uart.write('wasQuiet\n')
            else:
                display.clear()
            sleep(500)
        display.clear()
        if accelerometer.was_gesture('shake'):
            sounds = microphone.get_events()
            soundLevel = microphone.sound_level()
            print(soundLevel)
            for sound in sounds:
                if sound == SoundEvent.LOUD:
                    display.show(Image.SQUARE)
                elif sound == SoundEvent.QUIET:
                    display.show(Image.SQUARE_SMALL)
                else:
                    display.clear()
                print(sound)
                sleep(500)
