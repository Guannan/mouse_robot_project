#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)  #disables not at default(input)-pin-setting warnings

GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.OUT)
GPIO.setup (8, GPIO.OUT)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (25, GPIO.OUT)

wheel_tl = GPIO.PWM (4, 50)  # channel=12 frequency=50Hz
wheel_tr = GPIO.PWM (8, 50)
wheel_bl = GPIO.PWM (17, 50)
wheel_br = GPIO.PWM (22, 50)
# servo_side = 
# servo_bottom = 

wheel_tl.start (0)   # starting duty cycle
wheel_tr.start (50)
wheel_bl.start (50)
wheel_br.start (50)
try:
    while 1:
    	# going from dim to bright
        for dc in range(0, 101, 5):
            wheel_tl.ChangeDutyCycle (dc)
            wheel_tr.ChangeDutyCycle (98)
            wheel_bl.ChangeDutyCycle (98)
            wheel_br.ChangeDutyCycle (98)
            time.sleep(0.1)
        # going from bright to dim
        for dc in range(100, -1, -5):
            wheel_tl.ChangeDutyCycle(dc)
            wheel_tr.ChangeDutyCycle (2)
            wheel_bl.ChangeDutyCycle (2)
            wheel_br.ChangeDutyCycle (2)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
wheel_tl.stop()
wheel_tr.stop()
wheel_bl.stop()
wheel_br.stop()
GPIO.cleanup()
print 'process ended!'