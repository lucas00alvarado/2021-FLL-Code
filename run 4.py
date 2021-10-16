#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))
bot.gyro_sensor.reset()
time.sleep(0.05)
bot.gyro_straight(50,18,0.5)
bot.gyro_turn(35, 40, 26)
bot.gyro_straight(40, 20, 0.35)
bot.motor1.on_for_rotations(30,0.45)
bot.gyro_turn(-50, 20, 60)
bot.motor1.on_for_rotations(30,-0.45)
bot.gyro_turn(90, -20, -40)
bot.gyro_straight(50,44,0.5)
bot.gyro_turn(-80,0,20)
bot.motor1.on_for_rotations(30,0.45)
bot.gyro_turn(-50,20,60)
bot.motor1.on_for_rotations(-30,0.5)
bot.gyro_straight(-40,-20,0.5)
bot.gyro_turn(70,40,0)
bot.gyro_straight(40,15,0.5)
bot.gyro_turn(-15,0,40)
bot.gyro_straight(40,10,0.5)
print(bot.last_gyro_angle)
bot.gyro_turn(-90,0,20,buffer=4)
bot.stop_on_black(7,40)
bot.gyro_straight(20,5,0.5)