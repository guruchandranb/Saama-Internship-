from adafruit_circuitplayground.express import cpx
import time

RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
    for i in range(0, 10):
        cpx.pixels[i] = RED
        time.sleep(0.5)

    time.sleep(0.5)

    for i in range(0, 10):
        cpx.pixels[i] = BLUE
        time.sleep(0.5)
