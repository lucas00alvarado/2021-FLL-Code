#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))
bot.gyro_sensor.reset()
bot.gyro_turn(53, 40, 20)
bot.gyro_straight(40, 50, 0.5)
bot.gyro_turn(-55,40,40)
bot.on_for_rotations(20,20,0.3)
bot.motor1.on_for_rotations(100,0.6)