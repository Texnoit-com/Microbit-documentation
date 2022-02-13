Кнопка
-------

:download:`Скачать файл с классов <Push_Button.py>`

.. image:: Digital_Push_Button.png
    :width: 100px
    :align: center

Класс
*****

.. py:class::
    Push_Button
    
Класс используется для определения объектов, имеющих поведение кнопки 
    
Пример объявления объекта::

    button0=Push_Button(pin0)

.. py:function:: button0.is_pressed()

    Команда возвращает **True**, если кнопка нажата

.. py:function:: button0.click(time:int)

    Команда возвращает **True**, если кнопка была нажата-отжата ("клик")
    **time** - указывает паузу между состояниями нажата-отжата

.. py:function:: button0.count_pressed()

    Команда возвращает количество прошедших ее опросов методом **is_pressed()**,
    при которых кнопка была нажата

.. py:function:: button0.reset_pressed()

    Команда сбрасывает счетчик нажатий

Пример программы
****************

.. include:: sample.py
    :code: python