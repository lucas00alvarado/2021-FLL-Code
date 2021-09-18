#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from robot import Robot


bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, INPUT_3, OUTPUT_C, OUTPUT_D)

bot.gyro_sensor.reset()
# bot.double_follow_distance(30, 68.5, 0.4, kd=0.22)
bot.gyro_sensor.reset()
bot.gyro_straight(-30, -10, -0.25)
