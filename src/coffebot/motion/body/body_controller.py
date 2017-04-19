#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import warnings
import time

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from servo.servo_pca9685 import Servo

# set general params
ANGLE_OPEN_DISPENSER = 90
ANGLE_CLOSE_DISPENSER = 0

class Body(object):
    def __init__(self, _d_SERVO_ADDRESS, _emotion):
        # Candy dispenser position params
        self._d_SERVO_ADDRESS = _d_SERVO_ADDRESS
        self._d_servo_angle = 0
        self.d_servo = Servo(address =_d_SERVO_ADDRESS)

        # Body led params
        self._led_on = True
        self._backlight_color = '#ffffff'

        # other settings
        self._emotion = _emotion



        # move Body into default position
        self.set_dispenser_servo_position(self._d_servo_angle)


    def set_dispenser_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            angle: angle to turn servo, in degrees
        """
        if isinstance(angle, (int, float)):
            self.d_servo.set_angle(self._d_SERVO_ADDRESS, angle)
            self._d_angle = angle
        else:
            warnings.warn("'angle' param is not a number. Servo has not moved")


    def get_dispenser_servo_position(self):
        return (self._d_angle)


    def open_dispenser(self):
        self.set_dispenser_servo_position(ANGLE_OPEN_DISPENSER)

    def close_dispenser(self):
        self.set_dispenser_servo_position(ANGLE_CLOSE_DISPENSER)

    def give_candy(self):
        self.open_dispenser()
        time.sleep(0.5)
        self.close_dispenser()


    def set_emotion(self, emotion=None):
        if emotion is None:
            self._emotion = 'neutral'
        else:gis
            self._emotion = emotion

    def get_emotion(self):
        return self._emotion


    #TODO: Add implementation for methods below
    def set_led_mode(led_on=False, color=(255, 255, 255), mode='light', frequency=None):
        print('body: led_on={0},color={1}, mode={2}, frequency={3}'.format(led_on, color, mode, frequency))

    def blink_backlight(self, times: int):
        print('body backlight blink:', times)

    def set_backlight_color(self, color):
        print('body backlight color:', color)
        self.backlight_color = color

    def turn_backlight_on(self):
        print('body backlight on')

    def turn_backlight_off(self):
        print('body backlight off')

    def turn_backlight_dim(self):
        print('body backlight dim')