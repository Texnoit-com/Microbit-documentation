from microbit import (Image, SoundEvent, accelerometer, button_a, button_b,
                      display, microphone, sleep, uart)

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
