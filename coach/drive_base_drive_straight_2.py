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

inch = 20
speed = 300
distance_mm = inch * 25.4
timeToRun = (distance_mm*1000)/speed
for i in range(0,6):
    gyro1.reset_angle(0)
    wait(2000)
    if i%2 == 0:
        robot.drive_time(speed, 0, timeToRun)
    else:
        robot.drive_time(-1*speed, 0, timeToRun)
    robot.stop(Stop.BRAKE)
    wait(2000)
    print(str(gyro1.angle()))
