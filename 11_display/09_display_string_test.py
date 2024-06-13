import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':
    
    drone = Drone()
    drone.open()

    header = Header()

    header.dataType = DataType.DisplayDrawString
    header.length   = DisplayDrawString.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = DisplayDrawString()

    for i in range(0, 100, 1):

        data.x          = int(random.randint(0, 127))
        data.y          = int(random.randint(0, 63))
        data.font       = DisplayFont(int(random.randint(0, 1)))
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.message    = "HELLO"
        
        header.length   = DisplayDrawString.getSize() + len(data.message)

        dataArray = drone.transfer(header, data)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.03)
    
    drone.close()