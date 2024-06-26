from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventAttitude(attitude):
    print("eventAttitude() / {0:0.1f}, {1:0.1f}, {2:0.1f}".format(attitude.roll, attitude.pitch, attitude.yaw))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Attitude, eventAttitude)

    # Range 정보 요청
    drone.sendRequest(DeviceType.Drone, DataType.Attitude)
    sleep(0.1)

    drone.close()