from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventInformation(information):
    print("eventInformation()")
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


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Information, eventInformation)

    # Information 정보 요청
    drone.sendRequest(DeviceType.Controller, DataType.Information)
    sleep(0.1)

    drone.close()