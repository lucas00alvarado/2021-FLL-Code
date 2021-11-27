#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A,OUTPUT_B,56,15,INPUT_1,INPUT_2,
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
bot.gyro_turn(-45,0,30)
print(bot.gyro_sensor.angle)
print(bot.last_gyro_angle)
bot.gyro_straight(-15,-11,0.5)
print(bot.gyro_sensor.angle)
bot.motor2.on_for_rotations(20,0.1)
sleep(0.5)
bot.motor2.on_for_rotations(-20,0.1)
# Drops block in chicken's circle
bot.gyro_turn(36,20,1)
bot.follow_until_black(bot.right_sensor,bot.left_sensor,20,30,0.25,kd=0.08)
bot.gyro_turn(41,20,-6)
bot.gyro_turn(-45,0, 20)
bot.gyro_straight(20,3,0.5)
# Drops Package at Door
bot.gyro_straight(-42,-3,0.5)
bot.gyro_turn(18,0,-20)
bot.gyro_straight(-40,-3,0.5)
bot.gyro_turn(92,0,-20)
bot.gyro_straight(-40,-68,0.5)
# bot.gyro_turn(-30,0,30)
bot.motor2.on_for_rotations(20,0.1)
sleep(0.5)
bot.motor2.on_for_rotations(-20,0.1)
bot.gyro_straight(40,17,0.5)
bot.gyro_turn(58,40,10)
bot.gyro_straight(-40,-4,0.5)
bot.motor2.on_for_rotations(20,0.1)
sleep(0.5)
bot.motor2.on_for_rotations(-20,0.1)
bot.gyro_straight(40,8,0.25)
bot.motor1.on_for_rotations(10, 0.5)
bot.gyro_turn(100,40,7)
bot.gyro_straight(-20, -8, 0.5)
bot.gyro_straight(20, 3, 0.5)
bot.motor2.on_for_rotations(20,0.3)
sleep(0.5)
# bot.motor2.on_for_rotations(-20,0.1)
bot.last_gyro_angle = 301
bot.gyro_turn(-1, -20, 20)
bot.gyro_straight(30, 70, 0.5)
bot.gyro_turn(-45, 0, 20)
bot.gyro_straight(30, 70, 0.5)