#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((50, 50), 0, 16)

def driver ():
    while 1:
        event = pygame.event.poll()
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                break
            elif event.key == K_UP:
                print 'Up Arrow Pressed'
            elif event.key == K_DOWN:
                print 'Down Arrow Pressed'
            elif event.key == K_LEFT:
                print 'Left Arrow Pressed'
            elif event.key == K_RIGHT:
                print 'Right Arrow Pressed'

