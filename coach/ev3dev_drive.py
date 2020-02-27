#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor.lego import GyroSensor
import time
#
# https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/index.html
#
# motor
#m = LargeMotor(OUTPUT_B)
#m.on_for_rotations(SpeedPercent(75), 5)
gyro = GyroSensor()
gyro.mode = GyroSensor.MODE_GYRO_ANG
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
for i in range(0, 6):
    #
    # move steering
    #
    if (i % 2) == 0:
        steering_drive.on_for_degrees(0, SpeedPercent(50), 360*5, True)
    else:
        steering_drive.on_for_degrees(0, -1*SpeedPercent(50), 360*5, True)
    
    time.sleep(2)
    print('gyro:'+str(gyro.angle))