#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.black_value = 15
# sets the black value
bot.white_value = 90
# sets the white value
bot.gyro_sensor.reset()
# reset gyro sensor
sleep(0.05)
bot.gyro_turn(39, 40, -1)
# turn to angle of the line that will be followed later
bot.gyro_straight(40, 12, 0.5)
# drive to get to the line
bot.double_follow_distance(30, 67, 0.2, kd=0.35)
# follow the line while pushing the trucks
bot.last_gyro_angle = 90
# sets the bots current angle so that the next gyro moves will be from 90 degrees
bot.gyro_straight(-40, -10, 0.5)
# back up to release the trucks
bot.gyro_straight(30, 10, 0.5)
# goes forward to avoid transportation journey during the jog
bot.gyro_turn(47, 0, -40, buffer=4)
# first part of jog
bot.gyro_turn(-47, -40, 0, buffer=4)
# second part of jog
bot.gyro_straight(50, 77, 0.5)
# drive to knockover half of the bridge
bot.gyro_straight(-50, -25, 0.5)
# back up to knock over the other half of the bridge
# bot.gyro_straight(50, 3, 0.5)
bot.stop_on_black(15, 20)
# stop on the line that will be line followed
bot.gyro_turn(-22, 14, 30)
# turns to the angle of the line to follow
bot.follow_until_white(bot.right_sensor, bot.left_sensor, 30, 47, 0.1, kd=0.1)
# follows the line until right before the airdrop, on the white hash mark
bot.last_gyro_angle = 70
# makes the next gyro turn work
bot.gyro_turn(110, 20, -1.25)
# turns to the line to follow for train tracks
bot.single_follow_distance(bot.left_sensor, 20, 7, 42, 0.2, kd=0.08)
# follows line and pushes train to just before the gap
bot.motor1.on_for_rotations(-25, 0.25)
# brings the arm up so that it can go forward without touching the train
bot.gyro_straight(50, 15, 0.2, kd=0.08)
# goes forward to be in the right place to knock down the tracks
# bot.on_for_rotations(-10, 0, 0.04)
# turns to be in the right place to knock down the tracks
bot.motor1.on_for_rotations(-25, 0.25, brake=False)
# knocks down the train tracks
sleep(0.24)
# gives time for the tracks to fall
bot.motor1.on_for_rotations(50, 0.15)
# brings the arm back some so that it can go backwards without touching the train
# bot.on_for_rotations(10, 0, 0.05)
# turns to be straight again
bot.gyro_straight(-20, -14, 0.2, kd=0.08)
# goes backwards so that it can continue pushing the train
bot.motor1.on_for_rotations(50, 0.35)
# brings arm into position to push the train
bot.last_gyro_angle = 180
bot.gyro_straight(40, 37, 0.2, kd=0.08)
# pushes the train to the end of the tracks
bot.gyro_turn(-67.5, -40, -15)
# first part of backwards jog to be ready to pick up the blocks
bot.last_gyro_angle = 122.5
# makes it so that it will turn to 180 with the next turn
bot.gyro_turn(57.5, -7, -40)
# second part of backwards jog to be ready to pick up the blocks
bot.gyro_straight(-40, -15, 0.25, 0.0005, 0.08)
# backs up more to be ready to pick up the blocks
bot.motor1.on_for_rotations(-50, 0.18, brake=False)
# lowers the arm to be ready to pick up the blocks
bot.gyro_straight(20, 29, 1)
# goes forward so that the arm is in the blocks and ready to lift
bot.on_for_rotations(10, 10, -0.05)
# goes back a bit to unjam the blocks
bot.motor1.on_for_rotations(80, 1.9, brake=False)
# lifts the blocks
bot.motor1.on_for_rotations(-10, 0.2, brake=False)
print(bot.last_gyro_angle)
bot.gyro_turn(270 - bot.last_gyro_angle, 30, 0)
print(bot.gyro_sensor.angle, bot.last_gyro_angle)
# turns to 270 to face the bridge to be perpendicular to the line in front of it
bot.gyro_straight(-30, -3, 0.5)
bot.stop_on_black(15, 20)
print(bot.gyro_sensor.angle, bot.last_gyro_angle)
# stops on black to know it's position before going towards cargo ship
bot.gyro_turn(27, 20, -20)
# turns to be ready to go towards cargo ship
bot.gyro_straight(30, 63, 0.5)
# drives to have the cargo ship behind it
bot.gyro_turn(270 - bot.last_gyro_angle, 0, 20)
print(bot.gyro_sensor.angle, bot.last_gyro_angle)
# turns to be at 270, parallel to the cargo ship and perpendicular to the crane
bot.gyro_straight(-15, -26.5, 0.5)
print(bot.gyro_sensor.angle, bot.last_gyro_angle)
# drives back to push the crane
bot.gyro_straight(50, 20, 0.5)
bot.gyro_turn(-6.4, 0, 30)
bot.gyro_straight(60, 60, 0.5)
bot.gyro_turn(2.3, 30, 0)
bot.gyro_straight(60, 78, 0.5)
