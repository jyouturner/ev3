
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from threading import Thread

def reset_lifter_to_top():
    # move motor A until it press the touch sensor at top
    lifter_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, None)
    top_touch_sensor = TouchSensor(Port.S3)

    lifter_motor.run(360)
    while true:
        if top_touch_sensor.press():
            lifter_motor.stop()
            break
    # beep when it reach the top
    brick.sound.beep()

#main process

#move robot forward while raising the lifter to top
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

# create a new thread to run the other process that raise the lifter
t = Thread(target=reset_lifter_to_top)
t.start()

# drive straight for 120 millimeter at speed of 40 millimeter per second
drive_time_seconds = 120/40
drive_time_milliseconds = drive_time_seconds * 1000
robot.drive_time(40,0,drive_time_milliseconds)