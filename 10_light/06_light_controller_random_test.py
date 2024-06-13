import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    for i in range(0, 10, 1):
        
        colors = Colors(random.randint(0, Colors.EndOfType.value))

        dataArray = drone.sendLightModeColors(LightModeController.BodyDimming, 1, colors)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.6)
    
    drone.close()