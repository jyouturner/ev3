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

# create a variable to represent the Drive Base, which has functions to drive the robot, similiar to the DriveTank
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro1 = GyroSensor(Port.S1)
wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

gyro1.reset()

gyro_angle = gyro1.angle()
print(gyro_angle)
# make left turn until 120 degree
# drive left, at speed 40 milimeter per second, turning at 10 degree per second, to the left side
# robot.drive(40, -10)
while true:
    if(gyro1.angle() < -120):
        # stop driving
        robot.stop()
        break
# now drive straight
robot.drive(80,0)
