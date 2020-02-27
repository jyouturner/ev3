#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# create a variable to represent the touch sensor at port 3
touch3 = TouchSensor(Port.S3)

#TouchSensor has a function to return whether it is PRESSED or NOT
pressed = touch3.pressed
if pressed:
    print("someone pressed the touch sensor")
else:
    print("nobody is touching it")

