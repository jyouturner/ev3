#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# turn on bricks color orange
print("now show orange color...")
brick.light(Color.ORANGE)

wait(3000)

print("now turn off light...")
# Turn the light off
brick.light(None)

wait(3000)
print("now make a beep...")
# play sound A simple beep
brick.sound.beep()

wait(3000)

print("now make a long pitch...")
# A high pitch (1500 Hz) for one second (1000 ms) at 50% volume
brick.sound.beep(1500, 1000, 50)

print("now print hello world...")
# display hello world
brick.display.text("hello world", (40,50))

wait(5000)