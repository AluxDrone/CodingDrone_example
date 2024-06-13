from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventAck(ack):
    print("eventAck()")
    print("{0} / {1} / {2:04X}".format(ack.dataType.name, ack.systemTime, ack.crc16))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Ack, eventAck)

    # Ping 전송
    drone.sendPing(DeviceType.Controller)
    
    sleep(0.1)

    drone.close()