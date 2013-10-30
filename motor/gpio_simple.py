#!/usr/bin/env python

import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(7,gpio.OUT)
gpio.output(7,True)   # turns gpio pin7 HIGH
# gpio.output(7,False)  # turns gpio pin7 LOW



