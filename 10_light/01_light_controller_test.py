import random
from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.sendLightManual(DeviceType.Controller, 0xFF, 0)
    sleep(1);
    
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyRed.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyRed.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyRed.value, 0)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyGreen.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyGreen.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyGreen.value, 0)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyBlue.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyBlue.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, LightFlagsController.BodyBlue.value, 0)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000011, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000011, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000011, 0)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000110, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000110, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000110, 0)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000101, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000101, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Controller, 0b00000101, 0)
    sleep(1);


    drone.close()