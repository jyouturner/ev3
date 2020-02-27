#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from __future__ import division
import math
import sys

# create a variable to represent the Drive Base, which has functions to drive the robot, similiar to the DriveTank
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro1 = GyroSensor(Port.S1)
wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


# seems there is always like 5 degree over turn
angle = 90

#start from the slowest turn, which has the longest time like 3 seconds
time = 3000
while True:

    gyro1.reset_angle(0)
    wait(2000)
    steering = angle * (1000/time)
    dist = 2 * math.pi * (axle_track / 2) * (angle / 360) * (1000/time)
    robot.drive_time(-1 * dist, -1 * steering, time)

    print(str(time)+','+str(angle)+','+str(gyro1.angle()))
    robot.stop(Stop.BRAKE)
    wait(1000)
    time = time - 200
    if time < 100:
        break
