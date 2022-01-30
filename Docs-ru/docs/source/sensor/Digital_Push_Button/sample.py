from microbit import *
from Push_Button import Push_Button

button0=Push_Button(pin0)

while True:
    if button0.click(200):
        display.show(button0.count_pressed())
    if button0.count_pressed()>3:
        button0.reset_pressed()
        break
    sleep(200)
display.show(button0.count_pressed())
