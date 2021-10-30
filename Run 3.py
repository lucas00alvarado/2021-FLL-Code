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
bot.gyro_straight(40,95,0.5)
bot.gyro_turn(50,35,15)
bot.gyro_straight(30,11,0.5)
bot.gyro_turn(-45,0,20)
bot.gyro_straight(30,4,0.5)
bot.gyro_turn(50,0,-15)
bot.gyro_straight(-20,-3,0.5)