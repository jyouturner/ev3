#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# first we create a variable to represent the medium motor at port A with all default settings
medium_motor_A = Motor(Port.A)
# On for seconds
print("run medium motor for 5 seconds")
medium_motor_A.run_time(360, 5000, Stop.BRAKE)

# on for degree
print("run medium motor for 3600 degree, which is 10 rotations")
medium_motor_A.run_angle(360, 3600, Stop.BRAKE)

# on for degree
print("run medium motor for 3600 degree, which is 10 rotations, but the other direction")
medium_motor_A.run_angle(360, -3600, Stop.BRAKE)

# on for rotations
print("run medium motor for 3 rotations")
medium_motor_A.run_angle(360, 360*3, Stop.BRAKE)

# on
print("run medium motor continuouly...")
medium_motor_A.run(360)


wait(3000)

# off
print("then stop it")
medium_motor_A.stop(Stop.BRAKE)

print("run medium motor until it is stalled")
medium_motor_A.run_until_stalled(360, Stop.BRAKE)