#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A,OUTPUT_B,56,15,INPUT_1,INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C), motor2=LargeMotor(OUTPUT_D))

bot.motor1.reset()
bot.motor2.reset()
bot.last_gyro_angle = 0


bot.white_value = 95
bot.gyro_sensor.reset()
time.sleep(0.05)
bot.motor2.on_for_rotations(20,-0.1)
bot.gyro_turn(92,40,10)
bot.gyro_straight(60,85,1, angle=90)
bot.gyro_turn(40,40,5)
bot.stop_on_black(15,20)
bot.gyro_turn(-28,5,20)
bot.follow_until_white(bot.right_sensor, bot.left_sensor, 20, 35, 0.1, 0, 0.08)
bot.gyro_straight(40,2,0.5)
bot.gyro_turn(35,30,0)
bot.gyro_turn(-35,0, 30)
bot.gyro_straight(40,1,0.5)
# Drops Package at Door
bot.gyro_turn(93, -3, -20)
bot.gyro_straight(-60,-64,1)
bot.motor2.on_for_rotations(40,0.3)
sleep(0.5)
bot.motor2.on_for_rotations(-40,0.3)
#drops block in blue circle
bot.gyro_straight(40,17,0.5)
bot.gyro_turn(58,40,10)
bot.gyro_straight(-40,-4,0.5)
bot.motor2.on_for_rotations(40,0.3)
sleep(0.5)
bot.motor2.on_for_rotations(-40,0.3)
#drops in black circle
bot.gyro_straight(40,9,0.5)
bot.motor1.on_for_rotations(20, 0.5)
#turns arm
bot.gyro_turn(90,40,7)
bot.gyro_straight(-20, -9, 0.5)
bot.gyro_straight(20, 8, 0.5)
bot.motor2.on_for_rotations(40,0.3)
#drops block in cargo connect
bot.last_gyro_angle = 301
bot.gyro_turn(-21,0, 20)
# bot.gyro_straight(80, 75, 0.5)
# bot.gyro_turn(-30, -20, 20)
# bot.gyro_straight(80, 70, 0.5)
bot.motor1.on_for_rotations(0, 0, brake=False)
bot.motor2.on_for_rotations(0, 0, brake=False)