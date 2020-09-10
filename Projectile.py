import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
from math import *

import random

from EnemyObject import *
from BaseObjects import *
from Projectile import *


# Projectile class holds onto information about projectile
class Projectile:
    def __init__(self, position, motion):
        self.position = position                    # position of projectile
        self.motion = motion                        # motion of projectile
        self.oob = False                            # boolean variable, is true if projectile is out of window area

        self.projectiles = []
        self.enemyobjs = EnemyObject(Point(100, 100), Vector(0, 0))
        self.enemyobjls = []
        self.enemyobjlslim = 5
        
    def update(self, delta_time, win_x, win_y):
        
        # only update projectile if projectile is not outside window
        if self.oob == False:
            self.position += self.motion * delta_time
        if self.position.x > win_x or self.position.x < 0 or self.position.y > win_y or self.position.y < 0:
            # if projectile is outside the window set oob to True
            self.oob = True

    def display(self):
        # if projectile is outside of window, do not display the projectile
        if self.oob == False:

            glPushMatrix()

            glColor(random.random(), random.random(), random.random())

            glTranslate(self.position.x, self.position.y, 0)

            glBegin(GL_POINTS)
            glVertex2f(0, 0)
            glEnd()

            glPopMatrix()

