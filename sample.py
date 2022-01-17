#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor import *

from robot import *

bot = Robot(OUTPUT_A, OUTPUT_B, 56, 15, INPUT_1, INPUT_2,
            gyro_sensor_port=INPUT_3, motor1=LargeMotor(OUTPUT_C))

sleep(5)
bot.gyro_sensor.calibrate()
sleep(5)
bot.gyro_sensor.reset()
sleep(2)

# bot.motor1.on_for_rotations(10, 0.5)
# bot.motor1.on_for_rotations(0, 0, brake=False)
# bot.button.wait_for_bump('enter')
# bot.motor1.reset()
# bot.motor1.on_for_rotations(10, 0.5)