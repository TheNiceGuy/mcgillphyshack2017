# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:10:16 2017

@author: utilisateur1
"""
#Importing packages
import math
import numpy as np
from constants import *

class CelestialObject():
    '''Defining the abstract class celestial object who caracterize all spatial object in the simulation'''
    count = 0
    def __init__(self, x, y, vx, vy, mass, radius, x0=0, y0=0, ax=0, ay=0, collision=[], init=False):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.ax = ax
        self.ay = ay
        self.collisions = collision
        self.init = init
        self.index = CelestialObject.count
        CelestialObject.count += 1

    def distance(self, other_object):
        ''' Compute the distance between the celestial object and an other one (other object)'''
        d = math.sqrt((self.x - other_object.x)**2 + (self.y - other_object.y)**2)
        return d

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius

    def acceleration(self, objectList):
        ''' Compute the resulting acceleration on the celestial obeject '''
        self.ax = 0
        self.ay = 0
        for celest_object in objectList.values():
            if celest_object is self:
                pass
            else:
                self.ax += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_object.x - self.x)/self.distance(celest_object))
                self.ay += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_object.y - self.y)/self.distance(celest_object))

    def actualizeSystem(self, dt):
        ''' Actualize the system data: position, speed and state '''
        #If the system has not been initialize, do the first step with Euler method
        if not self.init:
            init = True
            #Change the speed with the acceleration using Euler method
            self.vx = self.vx + self.ax * dt
            self.vy = self.vy + self.ay * dt

            #Compute the position using the spedd and Euler's method
            x = self.x + self.vx * dt + (1/2) * self.ax * dt**2
            y = self.y + self.vy * dt + (1/2) * self.ay * dt**2

            #Update the values of the position (x,y) and old position (x0,y0)
            # 1) Old position
            self.x0 = self.x
            self.y0 = self.y

            # 2) New position
            self.x = x
            self.y = y

        #Else, use verlet integration method to actualize position and speed
        else:
            #Defining the new position
            x_t2 = 2 * self.x - self.x0 + self.ax * dt**2
            y_t2 = 2 * self.y - self.y0 + self.ay * dt**2

            #Defining the new speed with the new position
            self.vx = ((x_t2 - self.x0) / (2*dt))
            self.vy = ((y_t2 - self.y0) / (2*dt))

            #Updating the position
            # 1) Old positions
            self.x0 = self.x
            self.y0 = self.y

            # 2) New positions
            self.x = x_t2
            self.y = y_t2

    def collision(self, objectList):
        ''' Updates the list collision that contains the id of all the planets that collide with self'''
        for celest_object in objectList.values():
            if self.distance(celest_object) < 0.8*(self.radius + celest_object.radius) and (celest_object is not self):
                self.collisions.append(celest_object.index)

if __name__ == "__main__":
    pass
