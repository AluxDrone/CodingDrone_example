import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':
    
    drone = Drone()
    drone.open()

    header = Header()

    header.dataType = DataType.DisplayDrawCircle
    header.length   = DisplayDrawCircle.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = DisplayDrawCircle()

    for i in range(0, 100, 1):

        data.x          = int(random.randint(0, 127))
        data.y          = int(random.randint(0, 63))
        data.radius     = int(random.randint(0, 63))
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.flagFill   = bool(random.randint(0, 1))

        dataArray = drone.transfer(header, data)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.03)
    
    drone.close()