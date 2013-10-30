#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm_pin = GPIO.PWM(18, 50)  # channel=18 frequency=50Hz
pwm_pin.start(0)  # initially dimmed
try:
    while 1:   # infinitely do,
        for dc in range(0, 101, 5):   # duty cycle 0 -> 100 steps of 5
            pwm_pin.ChangeDutyCycle(dc)
            time.sleep (0.1)   # delay of 100ms
        for dc in range(100, -1, -5):   # duty cycle 100 -> 0  steps of 5
            pwm_pin.ChangeDutyCycle(dc)
            time.sleep (0.1)
except KeyboardInterrupt:  # Ctrl^C to stop
    pass
pwm_pin.stop()
GPIO.cleanup()
