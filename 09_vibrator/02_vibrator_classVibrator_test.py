from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    header = Header()
    
    header.dataType = DataType.Vibrator
    header.length   = Vibrator.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller

    data = Vibrator()

    data.mode       = VibratorMode.Instantally
    data.on         = 100
    data.off        = 200
    data.total      = 1200

    drone.transfer(header, data)
    sleep(1)


    drone.close()