# 드론 센서 캘리브레이션 요청 후 에러로 나타난 캘리브레이션 진행 상태를 화면에 표시
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def checkError(error, flag):
    if error & flag.value != 0:
        return True
    else:
        return False

def eventError(error):
    
    print("* eventError() / SystemTime({0:10}) / ErrorFlagsForSensor({1:032b}) / ErrorFlagsForState({2:032b})".format(error.systemTime, error.errorFlagsForSensor, error.errorFlagsForState))

    if checkError(error.errorFlagsForSensor, ErrorFlagsForSensor.Motion_Calibrating):
        print("    - MOTION 센서를 보정 중입니다.")


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Error, eventError)

    drone.sendPing(DeviceType.Controller)
    sleep(0.1)

    drone.sendCommand(CommandType.ClearBias)
    sleep(0.1)

    for i in range(30, 0, -1):
        print(i)
        sleep(1)

        error = drone.getData(DataType.Error)
        if error and not checkError(error.errorFlagsForSensor, ErrorFlagsForSensor.Motion_Calibrating):
            print("* MOTION 센서 보정이 완료되었습니다.")
            break

    drone.close()