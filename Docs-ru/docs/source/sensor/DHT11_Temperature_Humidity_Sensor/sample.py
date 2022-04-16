from microbit import *
from DHT11 import DHT11

i2c.init(sda=pin15, scl=pin13)
sensor = DHT11(i2c)

sensor.measure()
print(sensor.temperature())
print(sensor.humidity())
