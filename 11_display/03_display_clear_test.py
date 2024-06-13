import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    header = Header()
    
    header.dataType = DataType.DisplayClear
    header.length   = DisplayClear.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = DisplayClear()

    for i in range(0, 100, 1):

        data.width      = int(random.randint(0, 127))
        data.height     = int(random.randint(0, 63))
        data.x          = int(random.randint(0, 127) - data.width / 2)
        data.y          = int(random.randint(0, 63) - data.height / 2)
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))

        dataArray = drone.transfer(header, data)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.03)
    
    drone.close()