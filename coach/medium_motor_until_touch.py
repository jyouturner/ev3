#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# first we create a variable to represent the medium motor at port A with all default settings
medium_motor_A = Motor(Port.A)
touch4 = TouchSensor(Port.S4)

medium_motor_A.run(360)

while True:
    if touch4.pressed():
        print("raised to the top")
        medium_motor_A.stop()
        break
print("done")