#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))

bot.gyro_sensor.reset()
bot.gyro_straight(25, 50, 0.25)
# drives straight 60cm
bot.gyro_turn(-90, -20, 20)
# turns -90 degrees
bot.gyro_straight(25, 22, 0.25, angle=bot.gyro_sensor.angle)
# drives straight 18cm
bot.gyro_turn(90, 20, -20)
# turns 90 degrees
bot.gyro_straight(25, 35, 0.25)
# drives straight 40cm
bot.gyro_turn(135, 20, -20)
# turns 135 degrees
bot.on(5,5)
bot.motor1.on_for_rotations(15, 0.55) 
bot.stop()
#moves arm down
