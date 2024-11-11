from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventAck(ack):
    print("eventAck()")
    print("-   DataType: {0}".format(ack.dataType.name))
    print("-      CRC16: 0x{0:04X}".format(ack.crc16))
    print("- SystemTime: {0}".format(ack.systemTime))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Ack, eventAck)
    sleep(0.01)


    drone.sendMotorSingle(1, Rotation.Clockwise, 300)
    sleep(2)

    drone.sendMotorSingle(1, Rotation.Clockwise, 500)
    sleep(2)

    drone.sendMotorSingle(1, Rotation.Clockwise, 600)
    sleep(2)

    drone.sendMotorSingle(1, Rotation.Clockwise, 500)
    sleep(2)

    drone.sendMotorSingle(1, Rotation.Clockwise, 300)
    sleep(2)

    drone.sendStop()
    sleep(0.1)


    drone.close()