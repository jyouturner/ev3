#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# first we create a variable to represent the large motor at port D with all default settings
large_motor_D = Motor(Port.D)
# On for seconds
large_motor_D.run_time(360, 5000, Stop.BRAKE)

# on for degree
large_motor_D.run_angle(360, 3600, Stop.BRAKE)

# on for rotations
large_motor_D.run_angle(360, 360*3, Stop.BRAKE)

# on
large_motor_D.run(360)

# wait for 3000 miliseconds, which is 3 seconds
wait(3000)

# off
large_motor_D.stop(Stop.BRAKE)