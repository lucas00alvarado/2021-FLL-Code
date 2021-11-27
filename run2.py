#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

bot.black_value = 7
# sets the black value
bot.white_value = 60
# sets the white value
bot.gyro_sensor.reset()
# reset gyro sensor
bot.gyro_turn(39, 40, 0)
# turn to angle of the line that will be followed later
bot.gyro_straight(40, 12, 0.5)
# drive to get to the line
bot.double_follow_distance(30, 64, 0.2, kd=0.12)
# follow the line while pushing the trucks
bot.last_gyro_angle = 90
# sets the bots current angle so that the next gyro moves will be from 90 degrees
bot.gyro_straight(-40, -10, 0.5)
# back up to release the trucks
bot.gyro_straight(30, 8, 0.5)
# goes forward to avoid transportation journey during the jog
bot.gyro_turn(44, 0, -40, buffer=4)
# first part of jog
bot.gyro_turn(-44, -40, 0, buffer=4)
# second part of jog
bot.gyro_straight(50, 72, 0.5)
# drive to knockover half of the bridge
bot.gyro_straight(-50, -20, 0.5)
# back up to knock over the other half of the bridge
bot.stop_on_black(7, 20)
# stop on the line that will be line followed
bot.gyro_turn(-22, 14, 30)
# turns to the angle of the line to follow
bot.follow_until_white(bot.right_sensor, bot.left_sensor, 30, 40, 0.1, kd=0.1)
# follows the line until right before the airdrop, on the white hash mark
bot.last_gyro_angle = 72
# makes the next gyro turn work
bot.gyro_turn(110, 20, -1.25)
# turns to the line to follow for train tracks
bot.single_follow_distance(bot.left_sensor, 20, 7, 45, 0.2, kd=0.08)
# follows line and pushes train to just before the gap
bot.motor1.on_for_rotations(-50, 0.2)
# brings the arm up so that it can go forward without touching the train
bot.gyro_straight(50, 15, 0.2, kd=0.08)
# goes forward to be in the right place to knock down the tracks
bot.on_for_rotations(-10, 0, 0.04)
# turns to be in the right place to knock down the tracks
bot.motor1.on_for_rotations(-25, 0.3, brake=False)
# knocks down the train tracks
sleep(0.24)
# gives time for the tracks to fall
bot.motor1.on_for_rotations(50, 0.15)
# brings the arm back some so that it can go backwards without touching the train
bot.on_for_rotations(10, 0, 0.04)
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
bot.gyro_turn(57.5, 3.5, -40)
# seconds part of backwards jog to be ready to pick up the blocks
bot.gyro_straight(-40, -20, 0.25, 0.0005, 0.08)
# backs up more to be ready to pick up the blocks
bot.motor1.on_for_rotations(-50, 0.18, brake=False)
# lowers the arm to be ready to pick up the blocks
bot.gyro_straight(20, 31, 0.8)
# goes forward so that the arm is in the blocks and ready to lift
bot.on_for_rotations(10, 10, -0.04)
# goes back a bit to unjam the blocks
bot.motor1.on_for_rotations(80, 3)
# lifts the blocks
print(bot.last_gyro_angle)
bot.gyro_turn(270 - bot.last_gyro_angle, 30, 0)
# turns to 270 to face the bridge to be perpendicular to the line in front of it
bot.stop_on_black(7, 20)
# stops on black to know it's position before going towards cargo ship
bot.gyro_turn(22, 20, -20)
# turns to be ready to go towards cargo ship
bot.gyro_straight(30, 60, 0.5)
# drives to have the cargo ship behind it
bot.gyro_turn(270 - bot.last_gyro_angle, 0, 20)
# turns to be at 270, parallel to the cargo ship and perpendicular to the crane
bot.gyro_straight(-20, -50, 0.5)
# drives back to push the crane
