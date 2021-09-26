#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.gyro_turn(43, 40, 10)
bot.gyro_straight(40, 12, 0.5)
bot.double_follow_distance(30, 62, 0.25)
bot.gyro_straight(-40, -30, 0.5)
bot.gyro_turn(30, 0, -40, buffer=3)
bot.gyro_turn(-30, -40, 0, buffer=3)
bot.gyro_straight(20, 80, 0.5)
bot.gyro_straight(-40, -30, 0.5)
