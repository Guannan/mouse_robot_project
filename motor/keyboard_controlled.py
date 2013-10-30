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

    def duty_cycle (self, duty_cycle):
        self.dc = duty_cycle
        self.pwm.ChangeDutyCycle (duty_cycle)
        time.sleep (0.1)

    def direction (self, direction):
        self.direction = direction

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

def heardEnter ():
    i,o,e = select.select([sys.stdin],[],[],10)
    return i


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

    freq = 50

    wheel_tl = Wheel (wheel_tl_pin, 50, 1, freq)  # gpio pin pwm init (channel=4,frequency=50Hz), duty cycle init, direction init
    wheel_tr = Wheel (wheel_tr_pin, 50, 1, freq)
    wheel_bl = Wheel (wheel_bl_pin, 50, 1, freq)
    wheel_br = Wheel (wheel_br_pin, 50, 1, freq)
    # servo_side = 
    # servo_bottom = 

    try:
        while 1:
            i = heardEnter ()
            for s in i:
                if s == sys.stdin:
                    str_line = sys.stdin.readline().strip()
                    chars = list (str_line)
                    for char in chars:
                        if char == 'w':
                            print 'forward'
                        elif char == 'a':
                            print 'left'
                        elif char == 'd':
                            print 'right'
                        elif char == 's':
                            print 'back'
                            
            # time.sleep (0.1)
    except KeyboardInterrupt:
        pass

    wheel_tl.terminate ()
    wheel_tr.terminate ()
    wheel_bl.terminate ()
    wheel_br.terminate ()

    GPIO.cleanup()

