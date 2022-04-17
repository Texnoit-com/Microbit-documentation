from microbit import display, pin0, sleep

from Analog_Rotation import Analog_Rotation

rotation = Analog_Rotation(pin0)

display.scroll(str(rotation.get_signal()))
sleep(1000)

display.scroll(str(rotation.get_angle(800)))
sleep(1000)

display.scroll(str(rotation.get_scale(1000)))
sleep(1000)
