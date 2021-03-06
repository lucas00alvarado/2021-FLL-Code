from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.wheel import Wheel
from ev3dev2.button import Button
from time import sleep


class Robot(MoveTank):
    def __init__(self, left_motor_port, right_motor_port, wheel_diameter, wheel_width, left_sensor_port=None,
                 right_sensor_port=None, back_sensor_port=None, gyro_sensor_port=None, motor1=None,
                 motor2=None):
        """
A class that contains all of the functions that the ev3 should need to use. It has functionality for line followers, gyro sensor programs, driving, and more. Also contains all of the sensor and motor objects so that all of it only needs to be initialized once when the Robot class is initialized. Some of the methods inside of this class will only work if you have passed in the ports for all of the sensors and motors.
        :param left_motor_port: port for the left driving motor. Values: OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
        :param right_motor_port: port for the right driving motor. Values: OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
        :param wheel_diameter: the diameter of the wheels in millimeters
        :param wheel_width: the width of the wheels in millimeters
        :param left_sensor_port: port for the left color sensor. Values: INPUT_1, INPUT_2, INPUT_3, INPUT_4
        :param right_sensor_port: port for the right color sensor. Values: INPUT_1, INPUT_2, INPUT_3, INPUT_4
        :param back_sensor_port: port for the back color sensor. Values: INPUT_1, INPUT_2, INPUT_3, INPUT_4
        :param gyro_sensor_port: port for the gyro sensor. Values: INPUT_1, INPUT_2, INPUT_3, INPUT_4
        :param motor1: LargeMotor or MediumMotor object for one of the attachment motors.
        :param motor2: LargeMotor or MediumMotor object for one of the attachment motors.
        """
        super().__init__(left_motor_port, right_motor_port)
        self.gyro_sensor = GyroSensor(gyro_sensor_port)
        self.back_sensor = ColorSensor(back_sensor_port)
        self.left_sensor = ColorSensor(left_sensor_port)
        self.right_sensor = ColorSensor(right_sensor_port)
        self.left_motor = LargeMotor(left_motor_port)
        self.right_motor = LargeMotor(right_motor_port)
        self.wheel = Wheel(wheel_diameter, wheel_width)
        self.motor1 = motor1
        self.motor2 = motor2
        self.black_value = 10
        self.white_value = 50
        self.last_gyro_angle = 0
        self.button = Button()

    def pid_base_code(self, error, speed, kp, ki, kd, pid_variables):
        """
Provides the PID calculations that are then used in the line followers and gyro straight driving programs.
        :param error: calculated deviation from desired location
        :param speed: speed to drive at
        :param kp: sharpness of corrections
        :param ki: keeps driving in a straight line by keeping track of overall errors
        :param kd: decreases amount of swinging in the line follower or gyro straight driving program
        :param pid_variables: variables needed for integral and derivative to function
        :return: pid_variables with a few tweaks which will then be passed back in through pid_variables in the next loop iteration
        """
        proportional = error * kp
        integral = (error + pid_variables["integral"]) * ki
        derivative = (error - pid_variables["last_error"]) * kd
        correction = proportional + integral + derivative
        left_speed = speed - correction
        right_speed = speed + correction
        if abs(left_speed) > 100 or abs(right_speed) > 100:
            left_speed = (left_speed / abs(left_speed)) * 100
            right_speed = (right_speed / abs(right_speed)) * 100
        sleep(0.01)
        print("angle: ", self.gyro_sensor.angle)
        self.on(SpeedPercent(left_speed),
                SpeedPercent(right_speed))  # Super Function
        return {"integral": error + pid_variables["integral"], "last_error": error}

    def follow_until_black(self, color_sensor: ColorSensor, stop_sensor: ColorSensor, speed, rli, kp, ki=0, kd=0):
        """
Allows you to follow a line until the other color sensor hits black
        :param color_sensor: the color sensor object that you would like to follow the line
        :param stop_sensor: the color sensor object to detect black
        :param speed: speed for line following. Use a negative value to go backwards
        :param rli: the rli that you would like for the robot to try to stay on. Go to
        https://docs.google.com/document/d/1oJ3-Bsqdp4RnKgrdCS8U93gZ9PlmqChw0xg6aUa2zJY/edit?usp=sharing to learn more.
        :param kp: sharpness of corrections in the line follower.
        :param ki: makes sure that your corrections keep you on a straight line. DON'T USE WITH TURNS
        :param kd: keeps your turning from continuing to swing back and forth
        """
        pid_variables = {"integral": 0, "last_error": 0}
        while stop_sensor.reflected_light_intensity > self.black_value:
            error = rli - color_sensor.reflected_light_intensity
            pid_variables = self.pid_base_code(
                error, speed, kp, ki, kd, pid_variables)
        self.stop()  # Super Function

    def follow_until_white(self, color_sensor: ColorSensor, stop_sensor: ColorSensor, speed, rli, kp, ki=0, kd=0):
        """
Allows you to follow a line until the other color sensor hits white
        :param color_sensor: the color sensor object that you would like to follow the line
        :param stop_sensor: the color sensor object to detect white
        :param speed: speed for line following. Use a negative value to go backwards
        :param rli: the rli that you would like for the robot to try to stay on. Go to
        https://docs.google.com/document/d/1oJ3-Bsqdp4RnKgrdCS8U93gZ9PlmqChw0xg6aUa2zJY/edit?usp=sharing to learn more.
        :param kp: sharpness of corrections in the line follower.
        :param ki: makes sure that your corrections keep you on a straight line. DON'T USE WITH TURNS
        :param kd: keeps your turning from continuing to swing back and forth
        """
        pid_variables = {"integral": 0, "last_error": 0}
        while stop_sensor.reflected_light_intensity < self.white_value:
            error = rli - color_sensor.reflected_light_intensity
            pid_variables = self.pid_base_code(
                error, speed, kp, ki, kd, pid_variables)
        self.stop()  # Super Function

    def single_follow_distance(self, color_sensor: ColorSensor, speed, distance, rli, kp, ki=0, kd=0):
        """
Allows you to follow a line with 1 color sensor for a distance
        :param color_sensor: the color sensor object that you would like to follow the line
        :param speed: speed for line following. Use a negative value to go backwards
        :param distance: distance to line follow for in centimeters. Use a negative value to go backwards
        :param rli: the rli that you would like for the robot to try to stay on. Go to
        https://docs.google.com/document/d/1oJ3-Bsqdp4RnKgrdCS8U93gZ9PlmqChw0xg6aUa2zJY/edit?usp=sharing to learn more
        :param kp: sharpness of corrections in the line follower
        :param ki: makes sure that your corrections keep you on a straight line. DON'T USE WITH TURNS
        :param kd: keeps your turning from continuing to swing back and forth
        """
        self.left_motor.position = 0
        self.right_motor.position = 0
        pid_variables = {"integral": 0, "last_error": 0}
        tacho_distance = ((distance * 10) / self.wheel.circumference_mm) * 360
        if tacho_distance > 0:
            while abs(self.left_motor.position + self.right_motor.position) / 2 < abs(tacho_distance):
                # distance * 360(line above) converts rotations into tachocounts
                error = color_sensor.reflected_light_intensity - rli
                pid_variables = self.pid_base_code(
                    error, speed, kp, ki, kd, pid_variables)
            self.stop()  # Super Function
        else:
            while (self.left_motor.position + self.right_motor.position) / 2 > distance * 360:
                # distance * 360(line above) converts rotations into tachocounts
                error = color_sensor.reflected_light_intensity - rli
                pid_variables = self.pid_base_code(
                    error, speed, kp, ki, kd, pid_variables)
            self.stop()  # Super Function

    def double_follow_distance(self, speed, distance, kp, ki=0, kd=0):
        """
Allows you to follow a line with 2 color sensors for a distance
        :param speed: speed for line following
        :param distance: distance to line follow for in centimeters
        :param kp: sharpness of corrections in the line follower
        :param ki: makes sure that your corrections keep you on a straight line. DON'T USE WITH TURNS
        :param kd: keeps your turning from continuing to swing back and forth
        """
        self.left_motor.position = 0
        self.right_motor.position = 0
        pid_variables = {"integral": 0, "last_error": 0}
        tacho_distance = ((distance * 10) / self.wheel.circumference_mm) * 360
        while (self.left_motor.position + self.right_motor.position) / 2 < tacho_distance:
            error = self.right_sensor.reflected_light_intensity - \
                self.left_sensor.reflected_light_intensity
            pid_variables = self.pid_base_code(
                error, speed, kp, ki, kd, pid_variables)

    def gyro_straight(self, speed, distance, kp, ki=0, kd=0, angle=None, use_current_angle=False):
        """
Allows you to drive in a straight line using a gyro sensor
        :param speed: speed for driving. Use a negative value to go backwards
        :param distance: distance to drive for in centimeters. Use a negative value to go backwards
        :param kp: sharpness of corrections in your driving
        :param ki: makes sure that your corrections keep you on a straight line
        :param kd: keeps your turning from continuing to swing back and forth
        :param angle: the gyro sensor angle that you want to follow the line at. Auto set to the last gyro turn that you made
        :param use_current_angle: makes robot use current angle instead of the angle of the last gyro_turn
        """
        if not angle:
            angle = self.last_gyro_angle
        if use_current_angle:
            angle = self.gyro_sensor.angle
        self.left_motor.position = 0
        self.right_motor.position = 0
        tacho_distance = ((distance * 10) / self.wheel.circumference_mm) * 360
        pid_variables = {"integral": 0, "last_error": 0}
        while abs(self.left_motor.position + self.right_motor.position) / 2 < abs(tacho_distance):
           # print(tacho_distance, (self.left_motor.position +
           #       self.right_motor.position) / 2)
            error = self.gyro_sensor.angle - angle
            pid_variables = self.pid_base_code(
                error, speed, kp, ki, kd, pid_variables)
        self.stop()

    def gyro_turn(self, angle, left_speed, right_speed, buffer=2):
        """
Allows you to turn a specific angle using the gyro sensor.
        :param angle: gyro angle to turn. Use a negative value if turning counter-clockwise
        :param left_speed: the speed that the left wheel should drive at during the turn
        :param right_speed: the speed that the right wheel should drive at during the turn
        :param buffer: the amount of buffer in degrees that it can be on either side of the angle
        """
        if angle < 0:
            angle += self.last_gyro_angle
            while not (angle + buffer) > self.gyro_sensor.angle:
                self.on(SpeedPercent(left_speed), SpeedPercent(
                    right_speed))  # Super Function
            self.stop()
            self.last_gyro_angle = angle
        else:
            angle += self.last_gyro_angle
            while not (angle - buffer) < self.gyro_sensor.angle:
                self.on(SpeedPercent(left_speed), SpeedPercent(
                    right_speed))  # Super Function
            self.stop()
            self.last_gyro_angle = angle

    def square_line(self, speed):
        """
Allows the robot to square up on a black line so that the color sensors are parallel to the line
        :param speed: the speed to drive at during the square up
        """
        speed = SpeedPercent(speed)
        while self.left_sensor.color_name != "Black" and self.right_sensor.color_name != "Black":
            self.on(speed, speed)
        self.stop()
        while self.left_sensor.color_name != "Black":
            self.on(speed, 0)  # Super Function
        while self.right_sensor.color_name != "Black":
            self.on(0, speed)  # Super Function

    def stop_on_color(self, color_name, left_speed, right_speed, single_sensor=False, sensor=None):
        """
Allows you to have the robot drive and then stop on a certain color
        :param color_name: the color to stop on. Values: No color, Black, Blue, Green, Yellow, Red, White, and Brown
        :param left_speed: the speed that the left wheel should drive at
        :param right_speed: the speed that the right wheel should drive at
        :param single_sensor: whether it should be waiting for a specific sensor or for one of the front two
        :param sensor: the sensor to wait for if single_sensor is True
        """
        left_speed = SpeedPercent(left_speed)
        right_speed = SpeedPercent(right_speed)
        if single_sensor:
            while sensor.color_name != color_name:
                self.on(left_speed, right_speed)  # Super Function
        else:
            while self.left_sensor.color_name != color_name and self.right_sensor.color_name != color_name:
                self.on(left_speed, right_speed)  # Super Function

    def stop_on_black(self, black_value, speed):
        while self.left_sensor.reflected_light_intensity > black_value and self.right_sensor.reflected_light_intensity > black_value:
            self.on(speed, speed)
        self.stop()
