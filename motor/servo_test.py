#!/usr/bin/env python
import pygame
from pygame.locals import *
from motor_servo_ctrl import *   # importing created module from motor/servo control
import time

# main method
if __name__=="__main__":

    # initializing parameters
    GPIO.setwarnings(False)  #disables not at default(input)-pin-setting warnings
    GPIO.setmode(GPIO.BCM)
    servo_top_pin = 7  # servo top
    servo_bot_pin = 8  # servo bottom
    init_servo_duty_cycle = 30

    # pwm frequency (Hz)
    servo_freq = 180  # use to drive Tower- Pro SG-90 servo only

    # gpio pin pwm init (channel numbers, pin1 starting duty cycle, starting direction, pwm frequency)
    servo_tilt = Servo (servo_top_pin, init_servo_duty_cycle, servo_freq)
    servo_pan = Servo (servo_bot_pin, init_servo_duty_cycle, servo_freq)
    pan_tilt_control = Pan_Tilt (servo_pan, servo_tilt)

    # pygame interface used for getting keypresses without the need for 'enter' after each input
    pygame.init()
    screen = pygame.display.set_mode((50, 50), 0, 16)

    while 1:
        event = pygame.event.poll()
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                break
            elif event.key == K_UP:
                print 'Up Arrow Pressed'
                pan_tilt_control.tilt_change (5)
            elif event.key == K_DOWN:
                print 'Down Arrow Pressed'
                pan_tilt_control.tilt_change (-5)
            elif event.key == K_LEFT:
                print 'Left Arrow Pressed'
                pan_tilt_control.pan_change (-3)
            elif event.key == K_RIGHT:
                print 'Right Arrow Pressed'
                pan_tilt_control.pan_change (3)

    servo_tilt.terminate ()
    servo_pan.terminate ()
    GPIO.cleanup()

