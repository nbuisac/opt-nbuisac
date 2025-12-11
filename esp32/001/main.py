# main.py -- put your code here!
import machine, neopixel
from time import sleep_ms

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
colors_rgb = [
    (0, 255, 0),      # Verd
    (255, 0, 0),      # Vermell
    (0, 0, 255),      # Blau
    (255, 255, 0),    # Groc
    (128, 0, 128),    # Lila
    (255, 165, 0),    # Taronja
    (255, 192, 203)   # Rosa
]
n = 1    # number of pixels in your strip
p = 48   # GPIO number that will control the strip

np = neopixel.NeoPixel(machine.Pin(p), n)

while True:
    for c in colors_rgb:
        np[0] = c
        np.write()
        sleep_ms(500)


# Flashes three times in the order of Red, Green, and Blue for 0.5 seconds each, then turns off.

np[0] = (0, 0, 0)  # clear
np.write()