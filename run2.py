#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.black_value = 7
bot.gyro_sensor.reset()
bot.gyro_turn(43, 40, 10)
bot.gyro_straight(40, 12, 0.5)
bot.double_follow_distance(30, 63, 0.23, kd=0.02)
bot.gyro_straight(-40, -30, 0.5)
bot.gyro_turn(35, 0, -40, buffer=3)
bot.gyro_turn(-35, -40, 0, buffer=3)
bot.gyro_straight(50, 91, 0.5)
bot.gyro_straight(-50, -20, 0.5)
bot.stop_on_black(7, 20)
bot.gyro_straight(40, 5, 0.25)
bot.stop_on_black(7, 20)
bot.gyro_turn(-20, 7, 30)
bot.follow_until_black(bot.right_sensor, bot.left_sensor, 30, 35, 0.25)
