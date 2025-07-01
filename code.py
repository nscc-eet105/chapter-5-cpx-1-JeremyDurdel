#Jeremy Durdel
#Chapter 5 CPX 1
#Max Value 312
#Lowest Value 0

from adafruit_circuitplayground import cp
import time

def scale(value):
    MAX = 312
    maxIndex = 9
    index = int(value / MAX * maxIndex)
    return index

def off_pixels():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)

while True:
    light = cp.light
    index = scale(light)
    off_pixels()
    cp.pixels[index] = (0, 255, 0)
    print("Light:", light, "Index:")
    time.sleep(0.1)
