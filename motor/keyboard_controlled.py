#!/usr/bin/env python

import RPi.GPIO as GPIO
import time  # used for adding in delays
import sys
import select

class Wheel(object):
    def __init__(self, gpio_pin, init_duty_cycle, init_direction, init_freq):
        self.pin = gpio_pin
        self.freq = init_freq
        self.dc = init_duty_cycle
        self.direction = init_direction
        GPIO.setup (self.pin, GPIO.OUT)  # all wheel control signals are outputs, of course
        self.pwm = GPIO.PWM (self.pin, self.freq)
        self.pwm.start (init_duty_cycle)

    def set_duty_cycle (self, duty_cycle):
        self.dc = duty_cycle
        self.pwm.ChangeDutyCycle (duty_cycle)
        time.sleep (0.1)

    def get_duty_cycle (self):
        return self.dc

    def set_direction (self, direction):
        self.direction = direction

    def terminate (self):
        self.pwm.stop ()

# maybe use angle instead of duty_cycle
class Servo(object):
    def __init__(self, gpio_pin, init_duty_cycle, init_freq):
        self.pin = gpio_pin
        self.freq = init_freq
        self.dc = init_duty_cycle
        GPIO.setup (self.pin, GPIO.OUT)  # servo control, output
        self.pwm = GPIO.PWM (self.pin, self.freq)
        self.pwm.start (init_duty_cycle)

    def set_duty_cycle (self, duty_cycle):
        self.dc = duty_cycle
        self.pwm.ChangeDutyCycle (duty_cycle)
        time.sleep (0.1)

    def get_duty_cycle (self):
        return self.dc

    def terminate (self):
        self.pwm.stop ()

# need to make wheel a class
def move_forward ():
    wheel_tl.dc = 50
    wheel_tr.dc = 50
    wheel_bl.dc = 50
    wheel_br.dc = 50
    wheel_tl.direction = 1
    wheel_tr.direction = 1
    wheel_bl.direction = 1
    wheel_br.direction = 1

def move_back ():
    wheel_tl.dc = 50
    wheel_tr.dc = 50
    wheel_bl.dc = 50
    wheel_br.dc = 50
    wheel_tl.direction = -1
    wheel_tr.direction = -1
    wheel_bl.direction = -1
    wheel_br.direction = -1

def move_left ():
    wheel_tl.dc = 30
    wheel_tr.dc = 70
    wheel_bl.dc = 10
    wheel_br.dc = 60
    wheel_tl.direction = 1
    wheel_tr.direction = 1
    wheel_bl.direction = 1
    wheel_br.direction = 1

def move_right ():
    wheel_tl.dc = 30
    wheel_tr.dc = 70
    wheel_bl.dc = 60
    wheel_br.dc = 10
    wheel_tl.direction = 1
    wheel_tr.direction = 1
    wheel_bl.direction = 1
    wheel_br.direction = 1

def key_input ():
    i,o,e = select.select([sys.stdin],[],[],10)
    return i

def servo_sweep (servo_obj):
    my_dc = servo_obj.get_duty_cycle ()
    try:
        while 1:
            my_dc = my_dc + 5
            if (my_dc >= 100):
                my_dc = 10  # just to be safe, not turning to 0

            time.sleep (0.1)
            # print my_dc
            servo_obj.set_duty_cycle (my_dc)
    except KeyboardInterrupt:
        pass

# main method
if __name__=="__main__":

    # initializing parameters
    GPIO.setwarnings(False)  #disables not at default(input)-pin-setting warnings

    GPIO.setmode(GPIO.BCM)
    wheel_tl_pin = 4  # wheel top left
    wheel_tr_pin = 8  # wheel top right
    wheel_bl_pin = 17  # wheel bottom left
    wheel_br_pin = 22  # wheel bottom right
    servo_top_pin = 23  # servo top
    servo_bot_pin = 25  # servo bottom

    dc_motor_freq = 50
    servo_freq = 180  # use to drive SG-90 servo only

    wheel_tl = Wheel (wheel_tl_pin, 50, 1, dc_motor_freq)  # gpio pin pwm init (channel number, starting duty cycle, starting direction, pwm frequency)
    wheel_tr = Wheel (wheel_tr_pin, 50, 1, dc_motor_freq)
    wheel_bl = Wheel (wheel_bl_pin, 50, 1, dc_motor_freq)
    wheel_br = Wheel (wheel_br_pin, 50, 1, dc_motor_freq)
    servo_side = Servo (servo_top_pin, 50, servo_freq)
    servo_bottom = Servo (servo_bot_pin, 50, servo_freq)

    # performing test servo sweep...
    servo_sweep (servo_bottom)

    # i = key_input ()
    # for s in i:
    #     if s == sys.stdin:
    #         str_line = sys.stdin.readline().strip()
    #         chars = list (str_line)
    #         for char in chars:
    #             if char == 'w':
    #                 print 'forward'
    #             elif char == 'a':
    #                 print 'left'
    #             elif char == 'd':
    #                 print 'right'
    #             elif char == 's':
    #                 print 'back'
                            

    wheel_tl.terminate ()
    wheel_tr.terminate ()
    wheel_bl.terminate ()
    wheel_br.terminate ()
    servo_side.terminate ()
    servo_bottom.terminate ()
    GPIO.cleanup()

