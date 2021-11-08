#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C), motor2=LargeMotor(OUTPUT_D))

bot.gyro_sensor.reset()
time.sleep(0.05)
bot.motor2.on_for_rotations(20,-0.1)
bot.gyro_straight(20,4,0.5)
bot.gyro_turn(90,40,10)
print(bot.gyro_sensor.angle)
bot.gyro_straight(40,65,0.5)
bot.gyro_turn(30,40,5)
bot.gyro_straight(40,18.5,0.5)
bot.gyro_turn(-36,0,30)
print(bot.gyro_sensor.angle)
print(bot.last_gyro_angle)
bot.gyro_straight(-20,-7.5,0.5)
print(bot.gyro_sensor.angle)
bot.motor2.on_for_rotations(20,0.2)
sleep(1)
bot.motor2.on_for_rotations(-20,0.2)
bot.gyro_straight(20,6,0.5)
bot.gyro_turn(11.5,20,1)
bot.follow_until_black(bot.right_sensor, bot.left_sensor, 20, 35, 0.25, kd=0.08)
bot.gyro_turn(40,20,0)
bot.gyro_turn(-40,1, 20)
bot.gyro_straight(20,3,0.5)
bot.gyro_straight(-20,-3,0.5)
bot.gyro_turn(20,0,-20)
bot.gyro_straight(-20,-3,0.5)
bot.gyro_turn(87,0,-20)
bot.gyro_straight(-40,-70,0.5)
bot.motor2.on_for_rotations(20,0.2)
sleep(1)
bot.motor2.on_for_rotations(-20,0.2)
