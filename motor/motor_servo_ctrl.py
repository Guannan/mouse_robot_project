#!/usr/bin/env python

import RPi.GPIO as GPIO
import time  # used for adding in delays
import sys
# import select

class Wheel(object):
    def __init__(self, gpio_pin1, gpio_pin2, init_duty_cycle, init_direction, init_freq):
        self.pin1_num = gpio_pin1
        self.pin2_num = gpio_pin2
        self.freq = init_freq
        self.dc1 = init_duty_cycle  # pin 1 starts high, signals moving forward
        self.dc2 = 0  # pin 2 low for moving forward
        self.direction = init_direction  # 0: forward, 90: right, 180: backward, 270: left
        GPIO.setup (self.pin1_num, GPIO.OUT)  # all wheel control signals are outputs, of course
        GPIO.setup (self.pin2_num, GPIO.OUT)  # all wheel control signals are outputs, of course
        self.pwm_pin1 = GPIO.PWM (self.pin1_num, self.freq)  # positive means moving forward
        self.pwm_pin2 = GPIO.PWM (self.pin2_num, self.freq)  # positive means moving backward
        self.pwm_pin1.start (self.dc1)
        self.pwm_pin2.start (self.dc2)

    # immediately changes duty cycle
    def update_duty_cycle (self):
        self.pwm_pin1.ChangeDutyCycle (self.dc1)
        self.pwm_pin2.ChangeDutyCycle (self.dc2)
        time.sleep (0.1)

    def terminate (self):
        self.pwm_pin1.stop ()
        self.pwm_pin2.stop ()

    def slow_to_halt (self, pwm_pin, current_duty_cycle):
        # gradually lowers pwm until 0
        while (current_duty_cycle > 0):
            dc_change = round((float(current_duty_cycle) - 0)/2)
            current_duty_cycle -= dc_change
            update_duty_cycle (pwm_pin, current_duty_cycle)
            time.sleep (0.7)  #waits 0.7 second

    def accel_to_speed (self, pwm_pin, current_duty_cycle, final_duty_cycle):
        # gradually speeds up
        while (current_duty_cycle < final_duty_cycle):
            dc_change = round((float(final_duty_cycle) - float(current_duty_cycle))/2)
            current_duty_cycle += dc_change
            update_duty_cycle (pwm_pin, current_duty_cycle)
            time.sleep (0.7)  #waits 0.7 second

# maybe use angle instead of duty_cycle
class Servo(object):
    def __init__(self, gpio_pin, init_duty_cycle, init_freq):
        self.pin = gpio_pin
        self.freq = init_freq
        self.dc = init_duty_cycle
        GPIO.setup (self.pin, GPIO.OUT)  # servo control, output
        self.pwm = GPIO.PWM (self.pin, self.freq)
        self.pwm.start (init_duty_cycle)

    # TODO delete >> unnecessary wrapping
    def set_duty_cycle (self, duty_cycle):
        self.dc = duty_cycle
        self.pwm.ChangeDutyCycle (duty_cycle)
        time.sleep (0.1)

    def update_duty_cycle (self):
        self.pwm.ChangeDutyCycle (self.dc)
        time.sleep (0.1)

    # converts pwm duty cycle value to an angle 0 - 180 of servo horn
    def get_heading (self, duty_cycle):
        max_dc = 100.0
        max_angle = 180.0
        return (duty_cycle / max_dc) * max_angle

    # takes in degree change, either pos or neg
    def deg_to_duty_cycle (self, deg):
        max_dc = 100.0
        max_angle = 180.0
        return (deg / max_angle) * max_dc

    # degree_shift is the angle between image center and object center (depending on which servo, either horizontal or vertical dist)
    def shift_by_degree (self, degree_shift):
        dc_change = self.deg_to_duty_cycle (degree_shift)
        new_dc = self.dc + dc_change
        if (new_dc < 0):
            self.dc = 0
        elif (new_dc > 100):
            self.dc = 100
        else:
            self.dc = new_dc
        self.update_duty_cycle ()

    def terminate (self):
        self.pwm.stop ()

class Car(object):
    def __init__(self, wheel_tl, wheel_tr, wheel_bl, wheel_br):
        self.wheel_tl = wheel_tl
        self.wheel_tr = wheel_tr
        self.wheel_bl = wheel_bl
        self.wheel_br = wheel_br

    # hardcoded right now
    def move_forward ():
        self.wheel_tl.dc1 = 50
        self.wheel_tr.dc1 = 50
        self.wheel_bl.dc1 = 50
        self.wheel_br.dc1 = 50
        self.wheel_tl.dc2 = 0
        self.wheel_tr.dc2 = 0
        self.wheel_bl.dc2 = 0
        self.wheel_br.dc2 = 0
        self.wheel_tl.update_duty_cycle ()
        self.wheel_tr.update_duty_cycle ()
        self.wheel_bl.update_duty_cycle ()
        self.wheel_br.update_duty_cycle ()
        self.wheel_tl.direction = 0
        self.wheel_tr.direction = 0
        self.wheel_bl.direction = 0
        self.wheel_br.direction = 0

    # hardcoded right now
    def move_back ():
        self.wheel_tl.dc1 = 0
        self.wheel_tr.dc1 = 0
        self.wheel_bl.dc1 = 0
        self.wheel_br.dc1 = 0
        self.wheel_tl.dc2 = 50
        self.wheel_tr.dc2 = 50
        self.wheel_bl.dc2 = 50
        self.wheel_br.dc2 = 50
        self.wheel_tl.update_duty_cycle ()
        self.wheel_tr.update_duty_cycle ()
        self.wheel_bl.update_duty_cycle ()
        self.wheel_br.update_duty_cycle ()
        self.wheel_tl.direction = 180
        self.wheel_tr.direction = 180
        self.wheel_bl.direction = 180
        self.wheel_br.direction = 180

    # hardcoded right now
    def move_left ():
        self.wheel_tl.dc1 = 30
        self.wheel_tr.dc1 = 70
        self.wheel_bl.dc1 = 10
        self.wheel_br.dc1 = 60
        self.wheel_tl.dc2 = 0
        self.wheel_tr.dc2 = 0
        self.wheel_bl.dc2 = 0
        self.wheel_br.dc2 = 0
        self.wheel_tl.update_duty_cycle ()
        self.wheel_tr.update_duty_cycle ()
        self.wheel_bl.update_duty_cycle ()
        self.wheel_br.update_duty_cycle ()
        self.wheel_tl.direction = 270
        self.wheel_tr.direction = 270
        self.wheel_bl.direction = 270
        self.wheel_br.direction = 270

    # hardcoded right now
    def move_right ():
        self.wheel_tl.dc = 30
        self.wheel_tr.dc = 70
        self.wheel_bl.dc = 60
        self.wheel_br.dc = 10
        self.wheel_tl.dc2 = 0
        self.wheel_tr.dc2 = 0
        self.wheel_bl.dc2 = 0
        self.wheel_br.dc2 = 0
        self.wheel_tl.update_duty_cycle ()
        self.wheel_tr.update_duty_cycle ()
        self.wheel_bl.update_duty_cycle ()
        self.wheel_br.update_duty_cycle ()
        self.wheel_tl.direction = 90
        self.wheel_tr.direction = 90
        self.wheel_bl.direction = 90
        self.wheel_br.direction = 90

# def key_input ():
#     i,o,e = select.select([sys.stdin],[],[],10)
#     return i

class Pan_Tilt(object):
    def __init__(self, pan_servo, tilt_servo):
        self.pan_servo = pan_servo
        self.tilt_servo = tilt_servo
    
    def pan_change (self, deg_change):
        self.pan_servo.shift_by_degree (deg_change)

    def tilt_change (self, deg_change):
        self.tilt_servo.shift_by_degree (deg_change)

    def reset_pan_servo (self):
        self.pan_servo.dc = 50
        self.pan_servo.update_duty_cycle ()  # assuming initial position

    def reset_tilt_servo (self):
        self.tilt_servo.dc = 50
        self.tilt_servo.update_duty_cycle ()

def servo_sweep (servo_obj):
    my_dc = servo_obj.get_duty_cycle ()
    try:
        while 1:
            my_dc = my_dc + 5
            if (my_dc >= 100):
                my_dc = 10  # just to be safe, not turning to 0

            time.sleep (0.1)
            # print my_dc
            servo_obj.dc = my_dc
    except KeyboardInterrupt:
        pass

