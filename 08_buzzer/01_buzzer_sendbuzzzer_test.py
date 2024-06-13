from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    

    drone.sendBuzzer(BuzzerMode.Mute, BuzzerScale.Mute.value, 500)
    sleep(1)

    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)
    sleep(1)

    drone.sendBuzzer(BuzzerMode.Hz, 500, 500)
    sleep(1)


    drone.sendBuzzerMute(100)
    drone.sendBuzzerMuteReserve(100)
    sleep(1.2)


    drone.sendBuzzerScale(BuzzerScale.C5, 500)
    drone.sendBuzzerScaleReserve(BuzzerScale.D5, 500)
    sleep(1.2)


    drone.sendBuzzerHz(1000, 500)
    drone.sendBuzzerHzReserve(1200, 500)
    sleep(1.2)
    

    drone.close()