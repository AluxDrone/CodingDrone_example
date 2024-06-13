from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Trim, eventTrim)


    # 드론 비행 트림 설정 변경
    drone.sendTrim(10, 20, 30, 40)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(1)


    # 드론 비행 트림 설정 변경
    drone.sendTrim(0, 0, 0, 0)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(1)

    drone.close()