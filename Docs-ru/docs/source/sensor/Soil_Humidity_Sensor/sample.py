from microbit import *

from Soil_Humidity import Soil_Humidity

soil = Soil_Humidity(pin0)

while True:
     display.scroll(soil.get_signal())
