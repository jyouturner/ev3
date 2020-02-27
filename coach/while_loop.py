#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.beep()

# a while loop always check some "condition", when the condition is TRUE, then it will execute whatever INSIDE the loop
while true:
    #here the statements are INSIDE the loop, because of the indentation (by SPAE or TAB but dont mix)
    print("I am waiting....")
    # still inside the loop due to indentation
    print("still waiting")
#below is outside of the loop, because there is no indentation. This means all statements here and below will be only executed
#after loop is over
print("bye, will you see me?")


# create a variable named "x" and initilize it with value 1
x = 1
# wait while x is less than 10
while x<10:
    print("I am waiting")
    print("I am still waiting")
    # increase the x by 1
    x = x + 1
#below is only executed after the loop is over
print("now loop is done, what happened?")
print(x)