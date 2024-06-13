from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    
    drone.sendBuzzer(BuzzerMode.Mute, BuzzerScale.Mute.value, 100)
    sleep(0.2);
    
    drone.sendBuzzerScale(BuzzerScale.G4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.G4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.A4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.A4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.G4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.G4, 300);     sleep(0.4);
    drone.sendBuzzerScale(BuzzerScale.E4, 300);     sleep(0.4);

    drone.close()