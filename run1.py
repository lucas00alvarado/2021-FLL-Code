#!/usr/bin/env micropython

from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.gyro_sensor.reset()
time.sleep(0.05)
# bot.gyro_straight(45, 50, 0.25)
# print("drives straight 60cm")
# bot.gyro_turn(-92, -10, 10)
# print("turns -90 degrees")
# bot.gyro_straight(40, 26, 0.25)
# print("drives straight 18cm to push blue box")
# bot.gyro_turn(135, 20, -20)
# print("turns 135 degrees to be in position for plane")
# bot.gyro_straight(40, 12, 0.25,)
# print("drives straight 40cm")
# bot.motor1.on_for_rotations(15, 0.1)
# print("bot.gyro_turn(135, 20, -20")
# bot.on(3, 3)
# bot.motor1.on_for_rotations(25, 0.38)
# print("moves arm down and drives")
# bot.gyro_straight(-45, 15, 0.25)
# print("drives backwards")
# bot.motor1.on_for_rotations(25, -0.03)
# print("lifts arm a little bit")
# bot.gyro_turn(15, 25, 20, buffer=2)
# print("turns slightly")
# bot.gyro_straight(40, 32, 0.25)
# print("goes straight till box reaches green circle")
# bot.gyro_straight(-20, -3, 0.25)
# print("goes backwards")
# bot.motor1.on_for_rotations(25, -0.44)
# print("lifts arm a bit")
# bot.gyro_turn(-15, 20, 30)
# print("slight turn to get in position for switch engine")
# bot.gyro_straight(25, 4, 0.25)
# bot.gyro_turn(30, 50, 10)
# print("gets in arm position")
# bot.motor1.on_for_rotations(25, 0.45)
# print("lowers arm")
# bot.gyro_straight(20, 4, 0.25)
# print("goes forward")
# bot.motor1.on_for_rotations(25, -0.45)
# print("switches engine")
# bot.gyro_turn(-15, -30, 30)
# print("slight turn to be in position for drive home")
# bot.gyro_straight(-50, -70, 0.25)
# print("goes home")


bot.gyro_straight(50, 48.5, 0.25)
#goes straight out of home
bot.gyro_turn(42, 25, 0)
#turns to deliver green block
bot.gyro_straight(50, 12, 0.25)
#delivers block in green circle
bot.gyro_turn(-32, -25, 0)
#
bot.motor1.on_for_rotations(25, -0.2)
#
bot.gyro_straight(50,7, 0.25)
#
bot.gyro_turn(52, 25, 0)
bot.motor1.on_for_rotations(10, 0.17)
bot.gyro_straight(30, 6, 0.25)
bot.motor1.on_for_rotations(10, -0.2)
bot.gyro_turn(-5, -25, 0)
bot.gyro_straight(-30, -38.5, 0.5)
bot.gyro_turn(-15, 0, 25)
bot.motor1.on_for_rotations(20, 0.45)
bot.gyro_straight(-30, -3, 0.5 )
bot.motor1.on_for_rotations(-20,0.35)
bot.gyro_turn(45,30,0)
bot.gyro_turn(-37,0,30)
bot.gyro_straight(40,8,0.25)
bot.motor1.on_for_rotations(20,0.35)
bot.gyro_straight(-40,-7,0.25)
bot.motor1.on_for_rotations(-40,0.5)
bot.gyro_straight(-80,-40,0.25)
