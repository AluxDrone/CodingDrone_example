from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    print("TakeOff")
    drone.sendTakeOff()
    sleep(5)

    print("Stop")
    drone.sendStop()
    sleep(5)
    
    drone.close()