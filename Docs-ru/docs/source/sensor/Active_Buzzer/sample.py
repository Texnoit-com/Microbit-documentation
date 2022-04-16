from microbit import *
import music
from Active_Buzzer import Active_Buzzer

sound=Active_Buzzer(pin0)

sound.beep(2000)
sleep(1000)

sound.siren(2000)
sleep(1000)

sound.play(music.BLUES)
sleep(1000)

sound.play_time(music.BIRTHDAY, 3000)
