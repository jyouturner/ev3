#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# create a variable to represent the color sensor at port 2
print("please make sure to connect one color sensor to Port 2 on ev3")
color2 = ColorSensor(Port.S2)

print("checking color now...")
color_detected = color2.color()
print(color_detected)
print("checking reflection now...")
color_reflection = color2.reflection()
print(color_reflection)
