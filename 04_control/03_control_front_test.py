from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    print("TakeOff")
    drone.sendTakeOff()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Hovering")
    drone.sendControlWhile(0, 0, 0, 0, 3600)
    for i in range(3, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Go Front 1 meter")
    drone.sendControlPosition16(10, 0, 0, 5, 0, 0)
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Landing")
    drone.sendLanding()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)


    drone.close()