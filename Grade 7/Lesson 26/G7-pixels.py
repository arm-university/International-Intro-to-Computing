from microbit import *
import neopixel

num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix) 
np[8] = (0, 255, 0)
np[16] = (0, 255, 0)
np.show()