#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# create a variable to represent the color sensor at port 4
print("please make sure to connect touch sensor to Port 4 on ev3")
touch4 = TouchSensor(Port.S4)

while True:
    print("pretending doing somethig like raising attachment arm...");
    if touch4.pressed():
        print("raised to the top")
        break
print("done")
