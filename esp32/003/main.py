from machine import Pin
from neopixel import NeoPixel
from time import sleep

pixel = NeoPixel(Pin(48, Pin.OUT), 1)

pixel[0] = (100, 0, 0)
pixel.write()
sleep(1)
pixel[0] = (0, 100, 0)
pixel.write()
sleep(1)
pixel[0] = (0, 0, 100)
pixel.write()
sleep(1)