import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    header = Header()
    
    header.dataType = DataType.LightMode
    header.length   = LightModeColor.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = LightModeColor()

    data.mode.mode      = LightModeController.BodyDimming.value
    data.mode.interval  = 1

    for i in range(0, 10, 1):
        
        data.color.r    = int(random.randint(0, 255))
        data.color.g    = int(random.randint(0, 255))
        data.color.b    = int(random.randint(0, 255))

        dataArray = drone.transfer(header, data)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.6)
    
    drone.close()