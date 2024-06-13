# 조종기의 페어링 정보를 변경하고, 변경된 정보를 요청한 후 이벤트 핸들러를 통해 응답을 출력하는 예제
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventPairing(pairing):
    print("eventPairing()")

    print("Address: 0x{0:04X}{1:04X}{2:04X} / {0}.{1}.{2}".format(
        pairing.address0, 
        pairing.address1, 
        pairing.address2))

    print("Scramble: {0}".format(pairing.scramble))
    print("Channel: {0}".format(pairing.channel0))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Pairing, eventPairing)

    # 페어링 설정
    drone.sendPairing(DeviceType.Controller, 0x0005, 0x0006, 0x0007, 0x08, 0x09, 0x10, 0x11, 0x12)
    sleep(0.01)

    # 페어링데이터 요청
    drone.sendRequest(DeviceType.Controller, DataType.Pairing)
    sleep(0.1)
    
    drone.close()