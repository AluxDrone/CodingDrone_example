from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventState(state):
    print("{0}".format(state.modeControlFlight))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.State, eventState)


    # 비행 제어 모드를 ModeControlFlight.Position 으로 변경
    drone.sendModeControlFlight(ModeControlFlight.Position)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(0.1)


    # 비행 제어 모드를 ModeControlFlight.Attitude 으로 변경
    drone.sendModeControlFlight(ModeControlFlight.Attitude)
    sleep(1)

    # 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(0.1)


    drone.close()