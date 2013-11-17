#!/usr/bin/env python

from SimpleCV import Camera, Display
from time import sleep

# Initialize the camera
cam = Camera(prop_set={'width':320, 'height':240})
disp = Display(resolution=(320,240))

# Loop to continuously get images
while not disp.isDone():
    cam.getImage().rotate(180).save(disp)
    sleep(0.1)

