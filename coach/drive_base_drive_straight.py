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

inch = 10
speed = 220
while True:
    gyro1.reset_angle(0)
    wait(2000)
    distance_mm = inch * 25.4
    
    timeToRun = (distance_mm*1000)/speed
    
    robot.drive_time(speed, 0, timeToRun)
    robot.stop(Stop.BRAKE)
    wait(1000)
    print(str(inch)+ ',' + str(speed)+ ',' + str(gyro1.angle()))
    speed = speed + 30
    if speed >= 350:
        break
