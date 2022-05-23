Кнопки
*******

.. py::module:: microbit

На микроконтроллере есть две кнопки: ``button_a`` и ``button_b``.

Атрибуты
==========

.. py:attribute:: button_a

    ``Button`` объект, представляющий левую кнопку.

.. py:attribute:: button_b

    Представляет правую кнопку.

Класс
=======

.. py:class:: Button()

    Шаблон кнопки.

    .. note::
        Этот класс фактически недоступен пользователю, он используется только
        два экземпляра кнопок, которые уже инициализированы.


    .. py:method:: is_pressed()

        Возвращает ``True`` если кнопка ``button`` удерживается, и ``False``.

    .. py:method:: was_pressed()

        Возвращает ``True`` если была нажата кнопка с  последнего момента вызова этого метода.

    .. py:method:: get_presses()

        Возвращает общее количество нажатий кнопок и сбрасывает это общее количество.
        до нуля перед возвратом.

Примеры
=======

.. code::

    import microbit

    while True:
        if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
            microbit.display.scroll("AB")
            break
        elif microbit.button_a.is_pressed():
            microbit.display.scroll("A")
        elif microbit.button_b.is_pressed():
            microbit.display.scroll("B")
        microbit.sleep(100)
