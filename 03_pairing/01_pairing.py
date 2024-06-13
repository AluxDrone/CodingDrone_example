# 조종기의 페어링 정보를 변경하고, 변경된 정보를 요청한 후 응답을 기다려 출력하는 예제
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    # 페어링 설정
    drone.sendPairing(DeviceType.Controller, 0x0001, 0x0002, 0x0003, 0x04, 0x05, 0x06, 0x07, 0x08)
    sleep(0.01)

    # 페어링데이터 요청
    drone.sendRequest(DeviceType.Controller, DataType.Pairing)
    
    timeStart = time.time()

    while True:
        sleep(0.01)
        dataType = drone.check()
        
        if    dataType == DataType.Pairing:
            pairing = drone.getData(DataType.Pairing)

            print("Address: 0x{0:04X}{1:04X}{2:04X} / {0}.{1}.{2}".format(
                pairing.address0, 
                pairing.address1, 
                pairing.address2))

            print("Scramble: {0}".format(pairing.scramble))
            print("Channel: {0}".format(pairing.channel0))
            break

        if time.time() > timeStart + 1:
            break
    
    drone.close()