from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    drone.sendRequest(DeviceType.Controller, DataType.Information)

    timeStart = time.time()

    while True:
        sleep(0.01)
        dataType = drone.check()
        
        if dataType == DataType.Information:
            information = drone.getData(DataType.Information)
            print("ModeUpdate: {0}".format(information.modeUpdate))
            print("ModelNumber: {0}".format(information.modelNumber))
            print("Version: {0}.{1}.{2} / {3} / 0x{3:08X}".format(
                information.version.major,
                information.version.minor,
                information.version.build,
                information.version.v))
            print("Release Date: {0}.{1}.{2}".format(
                information.year,
                information.month,
                information.day))
            break

        if time.time() > timeStart + 1:
            break

    drone.close()