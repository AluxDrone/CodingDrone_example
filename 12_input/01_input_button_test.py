from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


def eventButton(button):
    print("eventButton() / " +
        "Button: 0b{0:16}, Event: {1:6}".format(bin(button.button)[2:].zfill(16), button.event.name))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Button, eventButton)

    drone.sendPing(DeviceType.Controller)

    for i in range(10, 0, -1):
        print(i)
        sleep(1)

    drone.close()