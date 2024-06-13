from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    print("BodyHold")
    drone.sendLightModeColor(LightModeController.BodyHold, 200, 200, 200, 0)
    sleep(2); 
    

    #sendLightModeColor
    print("BodyDimming 1")
    drone.sendLightModeColor(LightModeController.BodyDimming, 3, 200, 0, 200)
    sleep(3);
    
    #sendLightModeColors
    print("BodyDimming 2")
    drone.sendLightModeColors(LightModeController.BodyDimming, 3, Colors.Cyan)
    sleep(3);
    

    # sendLightEventColor*
    print("BodyDimming 3")
    drone.sendLightEventColor(LightModeController.BodyDimming, 3, 3, 200, 200, 200)
    sleep(3);
    
    # sendLightEventColors*
    print("BodyDimming 4")
    drone.sendLightEventColors(LightModeController.BodyDimming, 3, 3, Colors.Magenta)
    sleep(3);
    

    drone.close()