#import pygame
import pygame
from pygame.locals import *

#import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

#import random
import random

#import math functions
import math
from math import *

#import other project files
from BaseObjects import *
from Projectile import *
from EnemyObject import *
from Player import *


# Class to hold onto game
class AsteroidGame:

    #initializing function
    def __init__(self):
        #variables for window size
        self.win_x_size = 800
        self.win_y_size = 600

        # x and y coordinates if enemy object was to reach the top right window corner
        self.max_enenyobj_x = 800
        self.max_enemyobj_y = 600

        #global variables
        
        self.clock = None
        self.position = Point(100, 200)
        self.player = Player(Point(100, 100))
        self.clock = None
        self.clock  = pygame.time.Clock()
        self.game_end = False
        self.pressing_space = False
        self.enemyobjls = []
        self.enemyobjlslim = 5
        self.enemies_amount = 1
        self.score = 0  
        self.projectiles = []
        self.projectile_speed = 200
        
        

        # initialize the display
        pygame.display.init()
        pygame.display.set_mode((self.win_x_size, self.win_y_size), DOUBLEBUF|OPENGL)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.clock.tick()

    def createObject(self):
            if len(self.enemyobjls) <= self.enemies_amount - 1:
                self.enemyobjls.append(EnemyObject(Point(random.randint(0, 800), 500), Vector(0, 0)))

    # update function to update game and game logic
    def update(self):
        self.createObject()
        # the delta time 
        delta_time = self.clock.tick() / 1000.0
        
        if self.pressing_space and self.player.shooting:
            self.projectiles.append(Projectile(Point(self.player.position.x , self.player.position.y), 
                self.player.motion + Vector(-sin(self.player.angle * pi / 180.0), cos(self.player.angle * pi / 180.0)) * self.projectile_speed ))
        

        self.player.update(delta_time, self.win_x_size, self.win_y_size)
        
        #self.enemyobjs.update(delta_time)

        for projectile in self.projectiles:
            for enemyobj in self.enemyobjls:
                enemyobj.collide(projectile, delta_time)
            self.player.shooting = False
            
            projectile.update(delta_time, self.win_x_size, self.win_y_size)


        for enemyobj in self.enemyobjls:
            enemyobj.update(delta_time, self.player.position)
            if self.player.collide(enemyobj):
                self.game_end = True

        

    # display the ship and the projectiles and objects
    def display(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1.0, 1.0, 0.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glViewport(0, 0, self.win_x_size, self.win_y_size)
        gluOrtho2D(0, self.win_x_size, 0, self.win_y_size)

        glMatrixMode(GL_MODELVIEW)

        self.player.display()
        for enemyobject in self.enemyobjls:
            enemyobject.display()
        for projectile in self.projectiles:
            projectile.display()
        #self.enemyobjs.display()
        pygame.display.flip()
        
        

    def game_loop(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_q:
                    glClearColor(random(), random(), random(), 1.0)
                elif event.key == K_LEFT:
                     self.player.going_left = True
                elif event.key == K_RIGHT:
                     self.player.going_right = True
                elif event.key == K_UP:
                     self.player.going_up = True
                elif event.key == K_DOWN:
                     self.player.brake = True
                elif event.key == K_SPACE:
                    self.player.shooting = True
                    self.pressing_space = True
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                     self.player.going_left = False
                elif event.key == K_RIGHT:
                     self.player.going_right = False
                elif event.key == K_UP:
                     self.player.going_up = False
                elif event.key == K_DOWN:
                     self.player.brake = False

                     
                
                
        self.update()
        self.display()

    def start_game(self):
        while not self.game_end:
            self.game_loop()


if __name__ == "__main__":
    game = AsteroidGame()
    game.start_game()
