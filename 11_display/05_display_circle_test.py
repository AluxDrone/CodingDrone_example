import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone(True, False, False, True, True)
    drone.open()

    for i in range(0, 100, 1):

        x          = int(random.randint(0, 127))
        y          = int(random.randint(0, 63))
        radius     = int(random.randint(0, 63))
        pixel      = DisplayPixel(int(random.randint(0, 1)))
        flagFill   = bool(random.randint(0, 1))

        drone.sendDisplayDrawCircle(x, y, radius, pixel, flagFill)
        sleep(0.05)

    drone.close()