#imports
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

import random

import math
from math import *

import numpy

from BaseObjects import *
from Projectile import *


# class EnemyObject holds information about an enemy object
class EnemyObject:
    def __init__(self, position, motion):
        self.position = position                    # point position of enemy object
        self.motion = motion                        # vector motion of enemy object
        self.is_hit = False                         # boolean value for if enemy object is hit
        self.oob = False                            # boolean value, is true if object is outside of window
        self.size_of_enem_obj = 75

    def distance(self, a, b):
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def is_between(self, a, c, b):
        return self.distance(a,c) + self.distance(c,b) == self.distance(a,b)


    # check if projectile has collided with enemy object
    def collide_on_vertex(self, vertex, point_b, point_a, vec_c, delta_time, end_point_a, end_point_b):
        
        # get normal vector
        n = Vector(vertex.x, -vertex.y)
        # get vector that will be dot producted with n 
        vec_dot_to_n = Vector(point_b.x - point_a.x, point_b.y - point_a.y)
        # get T_hit
        t_hit = (numpy.dot([n.x, n.y], [vec_dot_to_n.x, vec_dot_to_n.y])) / numpy.dot([n.x, n.y], [vec_c.x, vec_c.y])

        # if t_hit is between 0 and delta time
        if t_hit > 0 and t_hit < delta_time:
            # get p_hit
            p_hit = point_a + vec_c * t_hit

            # if p_hit is between the end points of the vector
            if 0 < (numpy.dot([end_point_b.x - end_point_a.x, end_point_b.y - end_point_a.y], [p_hit.x - end_point_a.x, p_hit.y - end_point_a.y])) < (numpy.dot([end_point_b.x - end_point_a.x, end_point_b.y - end_point_a.y], [end_point_b.x - end_point_a.x, end_point_b.y - end_point_a.y])):
                # collision happened
                self.is_hit = True


    def collide_on_vector_2(self, point_a, point_b, projectile_point, projectile_vector, delta_time):
        
        n = Vector(-(point_b.y - point_a.y) , (point_b.x - point_a.x))

        vec_b_to_a = Vector(point_b.x - projectile_point.x, point_b.y - projectile_point.y)

        t_hit = (numpy.dot([n.x, n.y], [vec_b_to_a.x, vec_b_to_a.y]) / numpy.dot([n.x, n.y], [projectile_vector.x, projectile_vector.y]))

        if t_hit > 0 and t_hit < delta_time:
            p_hit = point_a + projectile_vector * t_hit  

            if self.is_between(point_a, p_hit, point_b):
                self.is_hit = True
            # if 0 < (numpy.dot([point_b.x - point_a.x, point_b.y - point_a.y], [p_hit.x - point_a.x, p_hit.y - point_a.y])) < (numpy.dot([point_b.x - point_a.x, point_b.y - point_a.y], [point_b.x - point_a.x, point_b.y - point_a.y])):
            #     # collision happened
            #     self.is_hit = True

        

    def collide(self, projectile, delta_time):
        point1 = Point(self.position.x, self.position.y)
        point2 = Point(self.position.x + self.size_of_enem_obj, self.position.y)
        point3 = Point(self.position.x, self.position.y + self.size_of_enem_obj)

        # check collision of the three vectors
        # self.collide_on_vertex(Vector((self.position.x + 75) - self.position.x  , ((self.position.y) - self.position.y )), Point(self.position.x, self.position.y), projectile.position, projectile.motion, delta_time, Point(self.position.x, self.position.y), Point(self.position.x + 75, self.position.y ) )
        # self.collide_on_vertex(Vector((self.position.x) - self.position.x  , ((self.position.y + 75) - self.position.y )), Point(self.position.x + 75, self.position.y), projectile.position, projectile.motion, delta_time, Point(self.position.x, self.position.y), Point(self.position.x, self.position.y + 75) )
        # self.collide_on_vertex(Vector((self.position.x) - self.position.x + 75  , ((self.position.y + 75) - self.position.y )), Point(self.position.x + 75, self.position.y), projectile.position, projectile.motion, delta_time, Point(self.position.x, self.position.y + 75), Point(self.position.x + 75, self.position.y) )
        self.collide_on_vector_2(point1, point2, projectile.position, projectile.motion, delta_time)
        self.collide_on_vector_2(point1, point3, projectile.position, projectile.motion, delta_time)
        self.collide_on_vector_2(point2, point3, projectile.position, projectile.motion, delta_time)


        

    # update enemy object
    def update(self, delta_time, player_position):
        
        # only update if object has either not been hit or has not exited the window frame
        if self.is_hit == False or self.oob == False:
            self.motion = Vector(player_position.x - self.position.x + random.randint(-5000, 5000), player_position.y - self.position.y + + random.randint(-5000, 5000))
            self.position += self.motion * delta_time


    # display enemy obeject
    def display(self):
        # only display if object has either not been hit or has not exited the window frame
        if self.is_hit == False or self.oob == True:

            glPushMatrix()

            glBegin(GL_TRIANGLES)
            glColor(0.0, 1.0, 0.0)
            # glVertex2f(self.position.x , self.position.y  )
            # glVertex2f(self.position.x - 25, self.position.y - 75 )
            # glVertex2f(self.position.x - 75, self.position.y - 25)
            
            glVertex2f(self.position.x , self.position.y  )
            glVertex2f(self.position.x + self.size_of_enem_obj, self.position.y )
            glVertex2f(self.position.x , self.position.y + self.size_of_enem_obj)
            

            glEnd()

            glPopMatrix()


            