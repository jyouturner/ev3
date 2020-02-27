#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# create a variable to represent the Drive Base, which has functions to drive the robot, similiar to the DriveTank
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro1 = GyroSensor(Port.S1)
wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# reset one of the motors current angle to 0, this way we can calculate how many angles it has run
left_motor.reset_angle()
#drive straight for 5 rotations
robot.drive(40, 0)
while true:
    # read left motor angle
    if left_motor.angle() > 5*360:
        robot.stop()
        break

# drive straight for 120 millimeter at speed of 40 millimeter per second
drive_time_seconds = 120/40
drive_time_milliseconds = drive_time_seconds * 1000
robot.drive_time(40,0,drive_time_milliseconds)


# make turn
# will this make 135 degree turn?
robot.drive(0, 45, 3000)
robot.stop(Stop.BRAKE)

# make pivot left turn
time = 500
steering = angle * (1000/time)
dist= 2* math.pi* (axleTrack/ 2) * (angle / 360) * (1000/time)
# left turn is negative steering
print('making left turn speed ' + str(dist))
robot.drive_time(dist, -1*steering, time)
robot.stop(Stop.BRAKE)


# create a varioable to represent the gyro sensor at port 1
gyro1 = GyroSensor(Port.S1)
gyro1.reset()
# drive left, at speed 40 millimeter per second, turning at 10 degree per second, to the left side
robot.drive(40, -10)
while true:
    if(gyro1.angle < -120):
         robot.stop()
         break
# now drive straight f9r 3 seconds
robot.drive(80,0, 3000)

# drive until stalled
robot.drive(80,0)

while true:
    if left_motor.stalled():
        robot.stop(Stop.BRAKE)
        break
