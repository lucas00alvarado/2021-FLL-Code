#!/usr/bin/env micropython

from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            INPUT_4, motor1=LargeMotor(OUTPUT_C))

bot.gyro_sensor.reset()
time.sleep(0.05)
bot.gyro_straight(45, 50, 0.25)
print("drives straight 60cm")
bot.gyro_turn(-92, -10, 10)
print("turns -90 degrees")
bot.gyro_straight(40, 26, 0.25)
print("drives straight 18cm")
bot.gyro_turn(135, 20, -20)
print("turns 135 degrees")
bot.gyro_straight(40, 12, 0.25,)
print("drives straight 40cm")
bot.motor1.on_for_rotations(15, 0.1)
print("bot.gyro_turn(135, 20, -20")
bot.on(3,3)
bot.motor1.on_for_rotations(15, 0.38)
print("moves arm down and drives")
bot.gyro_straight(-45, 15, 0.25)
print("drives backwards") 
bot.motor1.on_for_rotations(15, -0.03)
print("lifts arm a little bit")
bot.gyro_turn(15, 25, 20, buffer=2)
print("turns slightly")
bot.gyro_straight(40, 32, 0.25)
print("goes straight till box reaches green circle")
bot.gyro_straight(-20,-3,0.25)
print("goes backwards")
bot.motor1.on_for_rotations(15, -0.44)
print("lifts arm a bit")
bot.gyro_turn(-15,20,30)
print("slight turn to get in position for switch engine")
bot.gyro_straight(25,4,0.25)
bot.gyro_turn(30,50,10)
#gets in arm position  
bot.motor1.on_for_rotations(10,0.45)
#lowers arm
bot.gyro_straight(20,4,0.25)
#goes forward
bot.motor1.on_for_rotations(20,-0.45)
#switches engine 
bot.gyro_turn(-15,-30,30)
#slight turn
bot.gyro_straight(-40,-60,0.25)
#goes home
bot.stop()
