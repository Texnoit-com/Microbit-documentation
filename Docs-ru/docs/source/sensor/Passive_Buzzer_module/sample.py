import music
from microbit import pin0

from Passive_Buzzer import Passive_Buzzer

sound = Passive_Buzzer(pin0)
sound.play(music.BLUES)
sound.play_time(music.BIRTHDAY, 3000)
