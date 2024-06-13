from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventState(state):
    print("{0}".format(state.headless))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.State, eventState)


    # 드론을 Headless 설정을 Headless 모드로 변경
    drone.sendHeadless(Headless.Headless)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(1)


    # 드론을 Headless 설정을 Normal 모드로 변경
    drone.sendHeadless(Headless.Normal)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(1)

    drone.close()