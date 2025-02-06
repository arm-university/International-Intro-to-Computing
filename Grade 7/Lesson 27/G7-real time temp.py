from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin0, 24)

while True:
    temp = temperature()-8
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (255, 0, 0)
        np.show()
    for pixel_id in range(0, len(np)-temp):
        np[pixel_id] = (0, 0, 255)
        np.show()
    sleep(5000)
    np.clear()
        

	 