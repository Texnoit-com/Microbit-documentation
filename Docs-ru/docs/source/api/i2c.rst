Протокол I²C
------------

.. py:module:: microbit.i2c

Модуль ``i2c`` позволяет вам общаться с устройствами, подключенными к вашей плате.
с использованием протокола шины I²C. Может быть несколько устройств, подключенных
одновременно, и каждый из них имеет свой уникальный адрес. Фиксированный
для устройства или настроен на нем. Ваша плата действует как мастер I²C.

Используется 7-битная адресация для устройства. `<http://www.totalphase.com/support/articles/200349176-7-bit-8-bit-and-10-bit-I2C-Slave-Addressing>`_.

Это может отличаться от других решений, связанных с micro:bit.

Как Вы должны общаться с устройствами (какие байты отправлять и как интерпретировать ответы)
зависит от рассматриваемого устройства и описаны отдельно в документации к этому устройству.


Функции
*******

.. py:function:: init(freq=100000, sda=pin20, scl=pin19)

    Повторно инициализируйте периферийное устройство с указанной тактовой частотой ``freq`` на
    указанные контакты ``sda`` и ``scl``.

    .. warning::
        
        На плате micro:bit V1 изменение выводов I²C по умолчанию приведет к
        отключению акселерометра и компаса, так как они подключены
        внутри этих контактов. Это предупреждение не относится к **V2**
        пересмотр микро: бита, так как он имеет отдельные линии I²C
        <https://tech.microbit.org/hardware/i2c/>`
        


.. py:function:: scan()

    Просканируйте шину на наличие устройств. Возвращает список 7-битных адресов, соответствующих
    на те устройства, которые ответили на сканирование.


.. py:function:: read(addr, n, repeat=False)

    Прочитать ``n`` байт с устройства с 7-битным адресом ``addr``. Если ``repeat`` равно
    ``True``, стоповый бит посылаться не будет


.. py:function:: write(addr, buf, repeat=False)

    Записать байты из ``buf`` в устройство с 7-битным адресом ``addr``. Если
    ``repeat`` имеет значение ``True``, стоп-бит не отправляется.


Подключение
-----------

Вы должны соединить вывод ``SCL`` устройства с выводом 19 micro:bit, а
контакт ``SDA`` устройства к контакту micro:bit 20. Вы также должны подключить
заземление на землю micro:bit (контакт «GND»). Возможно, вам потребуется питание устройства
с помощью внешнего источника питания или micro:bit.

На линиях I²C платы есть внутренние подтягивающие резисторы, но если Вы используете длинные провода
или большое количество устройств, придется добавить дополнительные подтягивающие резисторы для 
обеспечения бесшумной связи.
