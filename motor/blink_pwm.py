#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # *BCM* or BOARD channel numbering system
GPIO.setup(18, GPIO.OUT)  # using GPIO pin 18

pwm_pin = GPIO.PWM(18, 0.5)  # 0.5 Hz frequency
pwm_pin.start(0)  # starting pwm rate
input('Press return to stop:')   # wait for termination
pwm_pin.stop()
GPIO.cleanup()
