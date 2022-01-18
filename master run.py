#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *
from time import sleep

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C), motor2=LargeMotor(OUTPUT_D))

bot.button.wait_for_bump('enter')
###########################################################################################

bot.black_value = 15
# sets the black value
bot.white_value = 90
# sets the white value
bot.gyro_sensor.reset()
# reset gyro sensor
sleep(0.25)
bot.motor2.on_for_rotations(20,-0.1)
bot.gyro_turn(40, 40, -1)
# turn to angle of the line that will be followed later
bot.gyro_straight(40, 12, 0.5)
# drive to get to the line
bot.double_follow_distance(30, 67, 0.2, kd=0.3)
# follow the line while pushing the trucks
bot.last_gyro_angle = 90
# sets the bots current angle so that the next gyro moves will be from 90 degrees
bot.gyro_straight(-40, -10, 2)
# back up to release the trucks
bot.gyro_straight(30, 10, 2)
# goes forward to avoid transportation journey during the jog
bot.gyro_turn(47, 0, -40, buffer=4)
# first part of jog
bot.gyro_turn(-47, -40, 0, buffer=4)
# second part of jog
bot.gyro_straight(50, 54, 0.5)
# drive to knockover half of the bridge
# bot.gyro_straight(-50, -25, 0.5)
# back up to knock over the other half of the bridge
# bot.gyro_straight(50, 3, 0.5)
bot.stop_on_black(10, 20)
# stop on the line that will be line followed
bot.gyro_turn(-22, 14, 30)
# turns to the angle of the line to follow
bot.follow_until_white(bot.right_sensor, bot.left_sensor, 40, 47, 0.13, kd=0.13)
# follows the line until right before the airdrop, on the white hash mark
bot.last_gyro_angle = 70
# makes the next gyro turn work
bot.gyro_turn(112, 30, -1.25)
# turns to the line to follow for train tracks
bot.single_follow_distance(bot.left_sensor, 20, 7, 42, 0.13, kd=0.13)
# follows line and pushes train to just before the gap
bot.motor1.on_for_rotations(-25, 0.25)
# brings the arm up so that it can go forward without touching the train
# bot.gyro_straight(50, 15, 0.2, kd=0.08)
bot.single_follow_distance(bot.left_sensor, 20, 9, 42, 0.13, kd=0.13)
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
bot.gyro_straight(-20, -10, 0.2, kd=0.08)
# goes backwards so that it can continue pushing the train
bot.motor1.on_for_rotations(50, 0.35)
# brings arm into position to push the train
bot.last_gyro_angle = 180
bot.gyro_straight(40, 36, 0.2, kd=0.08)
# pushes the train to the end of the tracks
bot.gyro_turn(-67.5, -40, -15)
# first part of backwards jog to be ready to pick up the blocks
bot.last_gyro_angle = 122.5
# makes it so that it will turn to 180 with the next turn
bot.gyro_turn(57.5, -2, -20)
# second part of backwards jog to be ready to pick up the blocks
bot.gyro_straight(-40, -13, 0.25, 0.0005, 0.08)
# backs up more to be ready to pick up the blocks
bot.motor1.on_for_rotations(-50, 0.18, brake=False)
# lowers the arm to be ready to pick up the blocks
bot.gyro_straight(20, 20, 1)
# goes forward so that the arm is in the blocks and ready to lift
bot.on_for_rotations(10, 10, -0.05)
# goes back a bit to unjam the blocks
bot.motor1.on_for_rotations(80, 0.18)
# bot.motor1.on_for_rotations(-10, 0.2, brake=False)
bot.gyro_straight(-30, -3, 0.5)
bot.gyro_turn(92, 20, -20)
bot.motor1.on_for_rotations(-2, 0.2, block=False)
# bot.gyro_straight(60, 100, 2)
# bot.gyro_turn(-40, 0, 30)
# bot.gyro_straight(60, 17, 0.5)
# bot.gyro_turn(38, 20, -20)
bot.gyro_straight(65, 150, 2)
bot.motor1.on_for_rotations(6, 0.2, block=False)
bot.gyro_straight(65, 50, 2)
# bot.gyro_turn(-25, -20, 20)
# bot.gyro_straight(65, 40, 2)
#bot.motor1.on_for_rotations(10, 0.2)
# bot.gyro_turn(28, 20, -20)
# bot.gyro_straight(80, 66, 5)
bot.motor1.on_for_rotations(0, 0, brake=False)
bot.motor2.on_for_rotations(0, 0, brake=False)

bot.button.wait_for_bump('enter')

###########################################################################################

bot.motor1.on_for_rotations(0, 0, brake=True)

###############################################################################################################################


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

bot.button.wait_for_bump('enter')

##########################################################################################

###############################################################################################################################


bot.gyro_sensor.reset()
bot.motor1.reset()
bot.motor2.reset()
bot.last_gyro_angle = 0
time.sleep(0.05)
bot.gyro_straight(50, 48.5, 0.25)

# goes straight out of home
bot.gyro_turn(42, 25, 0)
# turns to deliver green block
bot.gyro_straight(50, 12, 0.25)
# delivers block in green circle

#goes straight out of home
bot.gyro_turn(42, 25, 0)
#turns to deliver green block
bot.gyro_straight(50, 12, 0.25)
#delivers block in green circle

bot.gyro_turn(-32, -25, 0)
#
bot.motor1.on_for_rotations(25, -0.2)
#

bot.gyro_straight(50, 7, 0.25)

bot.gyro_straight(50,7, 0.25)

#
bot.gyro_turn(52, 25, 0)
bot.motor1.on_for_rotations(10, 0.17)
bot.gyro_straight(30, 6, 0.25)
bot.motor1.on_for_rotations(10, -0.2)
bot.gyro_turn(-5, -25, 0)
bot.gyro_straight(-40, -38.5, 0.5)
bot.gyro_turn(-17, 0, 25)
bot.motor1.on_for_rotations(20, 0.45)

bot.gyro_straight(-30, -3, 0.5)
bot.motor1.on_for_rotations(-20, 0.35)
bot.gyro_turn(45, 30, 0)
bot.gyro_turn(-37, 0, 30)
bot.gyro_straight(40, 8, 0.25)
bot.motor1.on_for_rotations(20, 0.35)
bot.gyro_straight(-40, -7, 0.25)
bot.motor1.on_for_rotations(-40, 0.5)
bot.gyro_straight(-80, -40, 0.25)

bot.button.wait_for_bump('enter')
###########################################################################################

bot.gyro_straight(-30, -3, 0.5 )
bot.motor1.on_for_rotations(-20,0.35)
bot.gyro_turn(47,30,0)
bot.gyro_turn(-37,0,30)
bot.gyro_straight(40,8,0.25)
bot.motor1.on_for_rotations(20,0.35)
bot.gyro_straight(-40,-7.5,0.25)
bot.motor1.on_for_rotations(-40,0.5)
bot.gyro_straight(-80,-40,0.25)
bot.motor1.on_for_rotations(0, 0, brake=False)
bot.motor2.on_for_rotations(0, 0, brake=False)

bot.button.wait_for_bump('enter')
###############################################################################################################################


bot.gyro_sensor.reset()
bot.motor1.reset()
bot.last_gyro_angle = 0
time.sleep(0.05)
bot.gyro_straight(50, 20, 0.5)
print("goes straight out of home area")
bot.gyro_turn(39, 40, 26)
print("turns toward the plane transportation journey")
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.gyro_straight(60, 14, 0.35)
print("goes straight until in position to move plane")
bot.motor1.on_for_rotations(30, 0.46)
print("moves arm down and latches onto plane")
bot.gyro_turn(-50, 0, 60)
print("turns plane out of holder")
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.motor1.on_for_rotations(30, -0.45)
print("arm lifts of plane")
bot.gyro_turn(78, -20, -40)
print("turns robot away and then towards the truck")
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.gyro_straight(60, 42, 0.5)
print("moves straight towards truck")
bot.gyro_turn(-56, 0, 20)
print("turns into correct position for truck")
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.gyro_straight(60, 1, 0.5)
bot.gyro_straight(60,1,0.5)
bot.motor1.on_for_rotations(30, 0.43)
print("lowers arm onto the truck")
bot.gyro_turn(-60, -3, 100)
print("turns truck out of holder")
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.motor1.on_for_rotations(-30, 0.5)
# bot.gyro_straight(-40, -20, 0.5)
bot.gyro_turn(-90 - bot.last_gyro_angle, -40, 10)
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.gyro_straight(-60, -25, 0.5)
bot.gyro_turn(90, 40, 0)
print(bot.last_gyro_angle, '  ', bot.gyro_sensor.angle)
bot.gyro_straight(40,12,0.5)
bot.gyro_turn(-80,-5,40)
bot.stop_on_black(11, 40)
bot.gyro_straight(20, 8, 0.5)