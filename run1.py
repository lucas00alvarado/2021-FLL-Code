#!/usr/bin/env micropython

from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))

bot.gyro_sensor.reset()
time.sleep(0.05)
bot.gyro_straight(45, 50, 0.25)
# drives straight 60cm
bot.gyro_turn(-92, -10, 10)
# turns -90 degrees
bot.gyro_straight(40, 26, 0.25)
# drives straight 18cm
bot.gyro_turn(134, 20, -20)
# turns 135 degrees
bot.gyro_straight(40, 12, 0.25,)
# drives straight 40cm
bot.motor1.on_for_rotations(15, 0.1)
#bot.gyro_turn(135, 20, -20)
bot.on(3,3)
bot.motor1.on_for_rotations(15, 0.4)
#moves arm down and drives
bot.gyro_straight(-45, 15, 0.25)
#drives backwards 
bot.motor1.on_for_rotations(15, -0.05)
#lifts arm a little bit
bot.gyro_turn(15, 25, 20, buffer=2)
#turns slightly 
bot.gyro_straight(40, 35, 0.25)
#goes straight till box reaches green circle 
bot.motor1.on_for_rotations(15, -0.06)
#lifts arm a bit
bot.gyro_turn(-15,20,30)
bot.gyro_straight(25,3,0.25)
bot.gyro_turn(15,30,20)

#small turn
#bot.motor1.on_for_rotations(15,0.03)
#moves arm down very slightly 
#bot.gyro_straight(25,3,0.25)
#drives 3 cm straight 
#bot.motor1.on_for_rotations(15,-0.3)
bot.stop()
