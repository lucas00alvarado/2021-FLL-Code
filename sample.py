#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4,INPUT_3, motor1=LargeMotor(OUTPUT_C))
bot.gyro_sensor.reset()
bot.gyro_straight(20,20,0.5,0)
bot.gyro_turn(90, 30, -30)
bot.gyro_straight(20,20,0.25,0)