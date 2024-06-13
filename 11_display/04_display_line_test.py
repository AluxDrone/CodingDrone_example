import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    
    drone.sendDisplayClearAll(DisplayPixel(int(random.randint(0, 1))))
    sleep(0.1)

    for i in range(0, 100, 1):

        x1          = int(random.randint(0, 127))
        y1          = int(random.randint(0, 63))
        x2          = int(random.randint(0, 127))
        y2          = int(random.randint(0, 63))
        pixel       = DisplayPixel(int(random.randint(0, 1)))
        line        = DisplayLine(int(random.randint(0, 2)))

        dataArray = drone.sendDisplayDrawLine(x1, y1, x2, y2, pixel, line)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.02)
    
    drone.close()