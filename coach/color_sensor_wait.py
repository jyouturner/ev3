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
print("now you can put a RED color thing in front of the sensor...I am waiting...")


while True:
    #check the color sensor detection
    color_detected = color2.color()
    #check whether we see a RED color
    if color_detected == Color.RED:
        print("I see red color, stop waiting")
        break
    else:
        print("waiting for red color ...")
        continue
# after the loop
print("to be continued...")