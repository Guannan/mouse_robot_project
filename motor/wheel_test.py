#!/usr/bin/env python
import pygame
from pygame.locals import *
from motor_servo_ctrl import *   # importing created module from motor/servo control

# main method
if __name__=="__main__":

    # initializing parameters
    GPIO.setwarnings(False)  #disables not at default(input)-pin-setting warnings
    GPIO.setmode(GPIO.BCM)
    wheel_tl_pin1 = 17  # wheel top left
    wheel_tl_pin2 = 4  # for backward control
    # wheel_tr_pin1 = 21  # wheel top right
    wheel_tr_pin1 = 27  # apparently for R2 RPi, pin 21 is renamed as 27
    wheel_tr_pin2 = 22  # for backward control
    wheel_bl_pin1 = 18  # wheel bottom left
    wheel_bl_pin2 = 23  # for backward control
    wheel_br_pin1 = 24  # wheel bottom right
    wheel_br_pin2 = 25  # for backward control
    servo_top_pin = 7  # servo top
    servo_bot_pin = 8  # servo bottom
    init_wheel_duty_cycle = 0
    init_servo_duty_cycle = 30

    # directions in degrees
    dir_forward = 0
    dir_right = 90
    dir_backward = 180
    dir_left = 270

    # pwm frequency (Hz)
    dc_motor_freq = 50
    servo_freq = 180  # use to drive Tower- Pro SG-90 servo only

    # gpio pin pwm init (channel numbers, pin1 starting duty cycle, starting direction, pwm frequency)
    wheel_tl = Wheel (wheel_tl_pin1, wheel_tl_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_tr = Wheel (wheel_tr_pin1, wheel_tr_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_bl = Wheel (wheel_bl_pin1, wheel_bl_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_br = Wheel (wheel_br_pin1, wheel_br_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    # servo_side = Servo (servo_top_pin, init_servo_duty_cycle, servo_freq)
    # servo_bottom = Servo (servo_bot_pin, init_servo_duty_cycle, servo_freq)

    mouse_car = Car (wheel_tl,wheel_tr,wheel_bl,wheel_br)
    mouse_car.move_forward()

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
                mouse_car.move_forward ()
                mouse_car.decelerate ()
                print 'Up Arrow Pressed'
            elif event.key == K_DOWN:
                mouse_car.move_backward ()
                mouse_car.decelerate ()
                print 'Down Arrow Pressed'
            elif event.key == K_LEFT:
                mouse_car.move_left ()
                mouse_car.decelerate ()
                print 'Left Arrow Pressed'
            elif event.key == K_RIGHT:
                mouse_car.move_right ()
                mouse_car.decelerate ()
                print 'Right Arrow Pressed'
            
    wheel_tl.terminate ()
    wheel_tr.terminate ()
    wheel_bl.terminate ()
    wheel_br.terminate ()
    # servo_side.terminate ()
    # servo_bottom.terminate ()
    GPIO.cleanup()
