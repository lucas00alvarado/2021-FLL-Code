#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.black_value = 7
bot.white_value = 60
# bot.gyro_sensor.reset()
# bot.gyro_turn(43, 40, 10)
# bot.gyro_straight(40, 12, 0.5)
# bot.double_follow_distance(30, 63, 0.23, kd=0.04)
# bot.gyro_straight(-40, -30, 0.5)
# bot.last_gyro_angle = 90
# bot.gyro_turn(35, 0, -40, buffer=4)
# bot.gyro_turn(-35, -40, 0, buffer=4)
# bot.gyro_straight(50, 91, 0.5)
# bot.gyro_straight(-50, -20, 0.5)
# bot.stop_on_black(7, 20)
# bot.gyro_straight(40, 5, 0.25)
# bot.stop_on_black(7, 20)
# bot.gyro_turn(-20, 7, 30)
bot.motor1.on_for_rotations(10, 0.16)
bot.follow_until_white(bot.right_sensor, bot.left_sensor, 30, 40, 0.25)
bot.last_gyro_angle = bot.gyro_sensor.angle
bot.gyro_turn(-5, 0, 20)
bot.gyro_straight(40, 8, 0.1)
bot.gyro_turn(110, 30, -30)
bot.motor1.on_for_rotations(-10, 0.16)
bot.single_follow_distance(bot.left_sensor, 20, 30, 35, 0.3, kd=0.04)
# bot.gyro_straight(30, 30, 0.25)
bot.motor1.on_for_rotations(10, 0.5)
bot.motor1.on_for_rotations(-10, 0.5)
bot.gyro_straight(-30, -5, 0.5)
bot.motor1.on_for_rotations(10, 0.5)
bot.gyro_straight(30, 35, 0.25)
