from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    drone.sendVibrator(100, 200, 1200)
    sleep(1)

    drone.close()