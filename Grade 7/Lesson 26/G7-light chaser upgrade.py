from microbit import *
import neopixel
from random import randint


np = neopixel.NeoPixel(pin0, 24)

while True:
    
    for pixel_id in range(0, len(np)):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        np[pixel_id] = (red, green, blue)

        np.show()
        sleep(100)