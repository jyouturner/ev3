#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.beep()

# wait until one or more buttons are pressed, then exit the loop
buttons_pressed = {}
print("waiting for someone to press any button")
# keep waiting by the while loop
while True:
    # store the pressed buttons in the variable for later use
    buttons_pressed = brick.buttons()
    if any(buttons_pressed):
        print("someone pressed button, now we can stop waiting now...")
        # exit the loop
        break

# next is to investigate the buttons pressed earlier
print("ok some buttons are pressed, now let's print the id of them")
print(buttons_pressed)

print("now let's check one by one")

if Button.LEFT in buttons_pressed:
    print("left button is pressed")

if Button.RIGHT in buttons_pressed:
    print("right button is pressed")
