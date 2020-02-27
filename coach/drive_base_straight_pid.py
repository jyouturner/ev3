#!/usr/bin/env pybricks-micropython
#
# credit to https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51
#
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import print, wait
from pybricks.robotics import DriveBase
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
robot = DriveBase(left_motor, right_motor, 56, 114)
targetAG = 0
Kp = 0.5
Ki = 0
Kd = 0
error = 0
lastError = 0
intergral = 0
deriative = 0
while True:
    angle = gyro.angle()
    error = (targetAG - angle)
    direct = error * Kp
    intergral = (intergral + error) * Ki
    deriative = (error - lastError) * Kd
    turn = direct + intergral + deriative
    print("A",gyro.angle(),"P",direct,"I",intergral,"D",deriative, "sum",turn)
    lastError = error
    robot.drive(200,turn)
