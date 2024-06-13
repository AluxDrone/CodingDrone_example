from time import sleep

from CodingDrone.drone import *
from CodingDrone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    delay = 0.5
    
    drone.sendDisplayClearAll(DisplayPixel.Black)
    sleep(delay)

    drone.sendDisplayClear(59, 27, 10, 10, DisplayPixel.White)
    sleep(delay)

    drone.sendDisplayInvert(54, 22, 20, 20)
    sleep(delay)

    drone.sendDisplayDrawPoint(64, 32, DisplayPixel.White)
    sleep(delay)

    drone.sendDisplayDrawLine(10, 10, 118, 54, DisplayPixel.White, DisplayLine.Dotted)
    sleep(delay)

    drone.sendDisplayDrawRect(44, 12, 40, 40, DisplayPixel.White, False, DisplayLine.Dashed)
    sleep(delay)

    drone.sendDisplayDrawCircle(64, 32, 20, DisplayPixel.White, True)
    sleep(delay)
    
    drone.sendDisplayDrawString(10, 10, "HELLO", DisplayFont.LiberationMono5x8, DisplayPixel.White)
    sleep(delay)
    
    drone.sendDisplayDrawStringAlign(0, 128, 30, "CodingDrone", DisplayAlign.Center, DisplayFont.LiberationMono10x16, DisplayPixel.White)
    sleep(delay)
    
    drone.close()