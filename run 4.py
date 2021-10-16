#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))
bot.left_motor.ramp_up_sp=100
bot.right_motor.ramp_up_sp=100
#bot.left_motor.ramp_down_sp=500
#bot.right_motor.ramp_down_sp=500
bot.gyro_sensor.reset()
time.sleep(0.05)
bot.gyro_straight(40,18,0.5)
bot.gyro_turn(34, 40, 26)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.gyro_straight(40, 14, 0.35)
bot.motor1.on_for_rotations(30,0.45)
bot.gyro_turn(-50, 20, 60)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.motor1.on_for_rotations(30,-0.45)
bot.gyro_turn(90, -20, -40)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.gyro_straight(50,44,0.5)
bot.gyro_turn(-80,0,20)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.motor1.on_for_rotations(30,0.45)
bot.gyro_turn(-50,20,60)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.motor1.on_for_rotations(-30,0.5)
bot.gyro_straight(-40,-20,0.5)
bot.gyro_turn(80,40,0)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.gyro_straight(40,25,0.5)
bot.gyro_turn(-15,0,40)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.gyro_straight(40,25,0.5)
bot.gyro_turn(-90, 0, 20, buffer=4)
print(bot.last_gyro_angle, '  ' , bot.gyro_sensor.angle)
bot.stop_on_black(7,40)
bot.gyro_straight(20,5,0.5)