Речь 
------

Microbit умеет синтезировать речь по текстовому сообщению. Для этого используется
синтезатор речи.

Подключите библиотеку ``speech`` и вызовите функцию ``say``, передайте тектовое сообщение в нее::

    import speech

    speech.say("Hello, World")
В команде можно использовать параметры:

* ``pitch`` - высокий или низкий голос (0 = низкий, 255 = высокий)
* ``speed`` - скорость речи (0 = медленно, 255 = быстро)
* ``mouth`` - протяженность звуков (0 = закрытый звук, 255 = открытый звукы)
* ``throat`` - напряженность голоса (0 = расслабленный, 255 = напряженный)

Чтобы настроить параметры, вы передаете их в качестве аргументов функции ``say``

Пример::

    speech.say("I am a DALEK", speed=120, pitch=100, throat=100, mouth=200)

Создание длинной речи
+++++++++++++++++++++

Давайте напишем программу для речи::

    import speech
    import random
    from microbit import sleep

    # Генерируются случайные слова, которые вставляются в речь.
    location = random.choice(["brent", "trent", "kent", "tashkent"])
    action = random.choice(["wrapped up", "covered", "sang to", "played games with"])
    obj = random.choice(["head", "hand", "dog", "foot"])
    prop = random.choice(["in a tent", "with cement", "with some scent",
                         "that was bent"])
    result = random.choice(["it ran off", "it glowed", "it blew up",
                           "it turned blue"])
    attitude = random.choice(["in the park", "like a shark", "for a lark",
                             "with a bark"])
    conclusion = random.choice(["where it went", "its intent", "why it went",
                               "what it meant"])

    # формирование речи.
    poem = [
        "there was a young man from {}".format(location),
        "who {} his {} {}".format(action, obj, prop),
        "one night after dark",
        "{} {}".format(result, attitude),
        "and he never worked out {}".format(conclusion),
        "EXTERMINATE",
    ]

    # запуск фраз в цикле.
    for line in poem:
        speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
        sleep(500)

Фонемы
++++++++

Часто генератор речи воспроизводит английское слово неправильно. Для точного воспроизведения 
речи используются фонемы. 


Полный список фонем, которые понимает синтезатор речи, можно найти в английской
документации по API для речи ( https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html ).
В качестве альтернативы можно использовать функцию ``translate``.

Функция ``pronounce`` используется следующим образом::

    speech.pronounce("/HEH5EH4EH3EH2EH2EH3EH4EH5EHLP.”)