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

class Player:
    def __init__(self, position):
        
        self.max_enenyobj_x = 800
        self.max_enemyobj_y = 600
        self.position = position
        self.going_left = False
        self.going_right = False
        self.going_up = False
        self.brake = False
        self.shooting = False
        self.angle = 45
        self.motion = Vector(0, 0)        
        self.is_hit = False


    def collide(self, enemby_obj):
        if self.position.x <= enemby_obj.position.x and self.position.x >= enemby_obj.position.x - 37 and self.position.y <= enemby_obj.position.y and self.position.y >= enemby_obj.position.y - 37:
            return True
       

    def update(self, delta_time, win_x_size, win_y_size):

        # create enemy object
       
    
        # is user presses space, shoot projectile
        if self.shooting:
            pass
            # add projectile to projectile array
            
            # set so no more projectiles fire until user presses space again
            

         # if user presses left
        if self.going_left:
            #turn spaceship
            self.angle += 180 * delta_time
        
        # if user presses right
        if self.going_right:
            # turn spaceship right
            self.angle -= 180 * delta_time
            
        # if user presses up
        if self.going_up:
            # increase the motion vector so spaceship goes faster
            acceleration = Vector(-sin(self.angle * pi / 180.0), cos(self.angle * pi / 180.0))
            self.motion += acceleration * (delta_time * 100)

         # if user presses left
        if self.going_left:
            #turn spaceship
            self.angle += 180 * delta_time
        
        # if user presses right
        if self.going_right:
            # turn spaceship right
            self.angle -= 180 * delta_time
            
        # if user presses up
        if self.going_up:
            # increase the motion vector so spaceship goes faster
            acceleration = Vector(-sin(self.angle * pi / 180.0), cos(self.angle * pi / 180.0))
            self.motion += acceleration * (delta_time * 100)

        # check if spaceship is going outside of window, if so, reverse trajectory
        if (self.position.x >= win_x_size or self.position.x <= 0):
            self.motion.x = -self.motion.x

        if (self.position.y >= win_y_size or self.position.y <= 0):
            self.motion.y = -self.motion.y

        # if user presses down, slow down ship motion
        if self.brake:
            # check to make sure ship doesn't reverse if slowed down too much
            if self.motion.x > 0:
                self.motion.x += sin(self.angle * pi / 180.0) * (delta_time * 100)

            if self.motion.y > 0:
                self.motion.y += -cos(self.angle * pi / 180.0) * (delta_time * 100)

        # set a speed limit
        if self.motion.x < 250 or self.motion.y < 250:
            self.position += self.motion * delta_time


        # update projectile logic
        
            #self.enemyobjs.collide(projectile.position)

        # update enemy object logic
        


    def display(self):
        glPushMatrix()

        glTranslate(self.position.x, self.position.y, 0)
        glRotate( self.angle, 0, 0, 1)

        glBegin(GL_TRIANGLES)
        glColor(1.0, 0.0, 0.0)
        glVertex2f(-25, -25)
        glVertex2f(0, 50)
        glVertex2f(25, -25)
        glEnd()
        

        glPopMatrix()

        glPointSize(4)

        
            
        



    
