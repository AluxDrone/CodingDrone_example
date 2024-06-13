import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    for i in range(0, 100, 1):

        width      = int(random.randint(0, 127))
        height     = int(random.randint(0, 63))
        x          = int(random.randint(0, 127) - width / 2)
        y          = int(random.randint(0, 63) - height / 2)
        pixel      = DisplayPixel(int(random.randint(0, 1)))
        flagFill   = bool(random.randint(0, 1))
        line       = DisplayLine(int(random.randint(0, 2)))

        dataArray = drone.sendDisplayDrawRect(x, y, width, height, pixel, flagFill, line)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.03)
    
    drone.close()