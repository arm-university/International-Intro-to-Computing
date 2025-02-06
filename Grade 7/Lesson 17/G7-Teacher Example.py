# Add your Python code here. E.g.
from microbit import *

while True:
    readingx = accelerometer.get_x()
    readingy = accelerometer.get_y()
    readingz = accelerometer.get_z()
    
    if readingx > 20:
        display.show("R")
    elif readingx < -20:
        display.show("L")
        
    elif readingy > 20:
        display.show("U")    
    elif readingy < -20:
        display.show("D")
        
    elif readingz > 20:
        display.show("F")    
    elif readingz < -20:
        display.show("B")    
        
    else:
        display.show("-")