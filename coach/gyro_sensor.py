#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# create a varioable to represent the gyro sensor at port 1
gyro1 = GyroSensor(Port.S1)

gyro1.reset_angle(0)

current_angle = gyro1.angle()
print(current_angle)

print("now you can turn it to left side slowly ...")
while True:
    current_angle = gyro1.angle()
    print(current_angle)
    if current_angle < -30:
        print("ok it is beyond 30 degree to the left side, you can stop now")
        break

print("now you can turn it to right side slowly ...")
while True:
    current_angle = gyro1.angle()
    print(current_angle)
    if current_angle > 30:
        print("ok it is beyond 30 degree to the right side, you can stop now")
        break