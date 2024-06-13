from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    header = Header()
    
    header.dataType = DataType.Buzzer
    header.length   = Buzzer.getSize()
    header.from_    = DeviceType.Tester
    header.to_      = DeviceType.Controller


    data = Buzzer()

    data.mode       = BuzzerMode.Scale
    data.value      = BuzzerScale.C5.value
    data.time       = 500

    drone.transfer(header, data)
    sleep(1)


    data.mode       = BuzzerMode.Hz
    data.value      = 1200
    data.time       = 500

    drone.transfer(header, data)
    sleep(1)


    drone.close()