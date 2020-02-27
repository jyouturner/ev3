#!/usr/bin/env pybricks-micropython
#
# credit to https://medium.com/@marklucking/micropython-tutorial-xi-26799f151c65
#
from pybricks import ev3brick as brick
from pybricks.parameters import Button, Port, Stop
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.tools import wait
from pybricks.robotics import DriveBase
import sys

leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
wheelDiam = 56
wheelDist = 114
speed = 50
angle = 0
robot = DriveBase(leftMotor, rightMotor, wheelDiam, wheelDist)
while True:
    robot.drive(speed,angle)
    wait(1000)
    leftAngle = leftMotor.angle()
    rightAngle = rightMotor.angle()
    print(str(leftAngle)+ ','+str(rightAngle)+','+str(gyro.angle()))