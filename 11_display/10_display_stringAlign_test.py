import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    header = Header()

    header.dataType = DataType.DisplayDrawStringAlign
    header.length   = DisplayDrawStringAlign.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = DisplayDrawStringAlign()

    for i in range(0, 10, 1):

        data.x_start    = 0
        data.x_end      = 127
        data.y          = int(random.randint(0, 63))
        data.align      = DisplayAlign(int(random.randint(0, 2)))
        data.font       = DisplayFont(int(random.randint(0, 1)))
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.message    = "LOVE"

        header.length   = DisplayDrawStringAlign.getSize() + len(data.message)

        dataArray = drone.transfer(header, data)
        print("{0} / {1}".format(i, convertByteArrayToString(dataArray)))

        sleep(0.03)

    drone.close()