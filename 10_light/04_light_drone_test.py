from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.sendLightModeColor(LightModeDrone.BodyHold, 200, 0, 200, 200)
    sleep(1);


    # sendLightModeColor*
    drone.sendLightModeColor(LightModeDrone.BodyDimming, 3, 0, 0, 200)
    sleep(3);
    
    # sendLightModeColors*
    drone.sendLightModeColors(LightModeDrone.BodyDimming, 3, Colors.Cyan)
    sleep(3);
    

    # sendLightEventColor*
    drone.sendLightEventColor(LightModeDrone.BodyDimming, 3, 5, 200, 200, 200)
    sleep(3);
    
    # sendLightEventColors*
    drone.sendLightEventColors(LightModeDrone.BodyDimming, 3, 3, Colors.Magenta)
    sleep(3);
    

    drone.close()