#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

# bot.motor1.on_for_rotations(-50, 0.4, brake=False)
# bot.gyro_straight(20, 20, 0.25)
# bot.motor1.on_for_rotations(50, 1)
# bot.black_value = 7
bot.white_value = 60
bot.gyro_sensor.reset()
sleep(7)
# # reset gyro sensor
# bot.motor1.on_for_rotations(40, 0.2)
# bot.gyro_turn(45, 40, 10)
# # turn to angle of the line that will be followed later
# bot.gyro_straight(40, 12, 0.5)
# # drive to get to the line
# bot.double_follow_distance(30, 64, 0.15, kd=0.08)
# # follow the line while pushing the trucks
# bot.last_gyro_angle = 90
# # sets the bots current angle so that the next turn will be from 90 degrees
# bot.gyro_straight(-40, -30, 0.5)
# # back up before jogging the wheels to move further over for the bridge
# bot.gyro_turn(44, 0, -40, buffer=4)
# # first part of jog
# bot.gyro_turn(-44, -40, 0, buffer=4)
# # second part of jog
# bot.gyro_straight(50, 91, 0.5)
# # drive to knockover half of the bridge
# bot.motor1.on_for_rotations(-40, 0.2)

# bot.gyro_straight(-50, -20, 0.5)
# # back up to knock over the other half of the bridge
# bot.stop_on_black(7, 20)
# # stop on the hashmark before the line to line follow
# bot.gyro_straight(40, 5, 0.25)
# # goes past the hash mark to allow a stop on black to the line to follow
# bot.stop_on_black(7, 20)
# # stop on the line that will be line followed
# bot.gyro_turn(-20, 7, 30)
# # turns to the angle of the line to follow
# bot.motor1.on_for_rotations(10, 0.16)
# # puts the arm up so that it doesn't hit airdrop
# bot.follow_until_white(bot.right_sensor, bot.left_sensor,
#                        30, 40, 0.25, kd=0.04)
# # follows the line until right before the airdrop, on the white hash mark
# bot.last_gyro_angle = bot.gyro_sensor.angle
# # makes the next gyro turn work
# bot.gyro_turn(-5, 0, 20)
# # turns to get the right angle for hitting the airdrop
# bot.gyro_straight(40, 8, 0.1)
# # hits the airdrop
# bot.gyro_turn(110, 30, -30)
# # turns to the line to follow for train tracks
# bot.motor1.on_for_rotations(-10, 0.16)
# # brings arm down to be able to push the train
# bot.single_follow_distance(bot.left_sensor, 20, 30, 35, 0.15, kd=0.08)
# # follows the line, pushing the train and getting into position for knocking down the tracks
# bot.last_gyro_angle = 180
# # sets the gyro angle so that the next gyro straight is from 180 degrees
# bot.motor1.on_for_rotations(10, 0.35)
# # lowers the arm to knock down the train tracks
# bot.motor1.on_for_rotations(-10, 0.2)
# # bring arm back up, but not all the way to avoid hitting train with the back
# bot.gyro_straight(-30, -20, 0.5)
# # drives backwards to be ready to lower the front of the arm on to the train
# bot.motor1.on_for_rotations(10, 0.2)
# # lowers arm onto the front of the train
# bot.gyro_straight(30, 35, 0.25)
# # pushes the train the rest of the way
# bot.motor1.on_for_rotations(-10, 0.2)
# # brings the arm back up
# bot.gyro_turn(-90, -30, 0)
# # turns to go to the cargo ship
# bot.gyro_straight(-30, -27, 0.5)
# # drives backwards towards the bridge
# bot.gyro_turn(145, -13, -30)
# # turns to be ready to push the cargo ship
# bot.gyro_turn(82, 30, 15)
# # first part of jog to be closer to crane
# bot.gyro_turn(-47, 0, 30)
# # second part of jog to be closer to the crane
# bot.gyro_straight(-30, -29, 0.5)
# # drives backwards to push the cargo ship
# bot.gyro_turn(-10, 0, 20)
# # turns to be ready to go home
# bot.gyro_straight(60, 170, 0.5)
# # returns to home


bot.follow_until_white(bot.right_sensor, bot.left_sensor,
                       30, 40, 0.2, kd=0.08)
# follows the line until right before the airdrop, on the white hash mark
bot.last_gyro_angle = bot.gyro_sensor.angle
# makes the next gyro turn work
bot.gyro_turn(-5, 0, 20)
# turns to get the right angle for hitting the airdrop
bot.gyro_straight(40, 8, 0.1)
# hits the airdrop
bot.gyro_turn(110, 30, -30)
# turns to the line to follow for train tracks
bot.single_follow_distance(bot.left_sensor, 20, 17, 45, 0.2, kd=0.08)
bot.motor1.on_for_rotations(-50, 0.15)
bot.last_gyro_angle = bot.gyro_sensor.angle
bot.gyro_straight(50, 15, 0.2, kd=0.08)
# bot.gyro_turn(2, 20, 0)
bot.on_for_rotations(10, 0, 0.03)
bot.motor1.on_for_rotations(-25, 0.35, brake=False)
sleep(0.25)
bot.motor1.on_for_rotations(50, 0.15)
# bot.gyro_turn(-2, -20, 0)
bot.gyro_straight(-20, -14, 0.2, kd=0.08)
bot.motor1.on_for_rotations(50, 0.35)
bot.gyro_straight(40, 36.5, 0.2, kd=0.08)
bot.gyro_turn(-67.5, -40, -15)
bot.gyro_turn(57.5, 0, -40)
bot.gyro_straight(-40, -20, 0.25, 0.0005, 0.08)

bot.motor1.on_for_rotations(-50, 0.4, brake=False)
bot.last_gyro_angle = 0
bot.gyro_straight(20, 30, 0.25)
bot.motor1.on_for_rotations(20, 1, brake=False)
