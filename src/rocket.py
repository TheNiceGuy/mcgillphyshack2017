# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:10:16 2017

@author: utilisateur1
"""
from constants import *
from celestial_object import *
import numpy as np
from systeme_solaire import *

class Rocket(CelestialObject):
    '''defining the rocket class that caracterizes the rocket in the simulation'''

    def __init__(self, mass, radius, Parent_index,Parent, theta0, theta, x=0, y=0, vx=0, vy=0, grounded=True,  qte_gas=200*1000, ejection_speed=4000, mass_flow=1000, propulsion=False):
        super().__init__(x, y, vx, vy, mass, radius)
        self.qte_gas = qte_gas
        self.ejection_speed = ejection_speed
        self.mass_flow = mass_flow
        self.Parent_index=Parent_index
        self.grounded=grounded
        self.propulsion=propulsion
        self.x=Parent.x+(radius+Parent.radius)*(np.cos(theta0))
        self.y=Parent.y+(radius+ Parent.radius)*np.sin(theta0)
        self.vx = 0
        self.vy = 0
        #self.vx = Parent.w*Parent.radius * np.cos(np.pi/2-theta0)
        #self.vy = Parent.w*Parent.radius * np.sin(np.pi/2-theta0)
        self.Parent=Parent
        self.theta = theta0


        self.theta0=theta0
    def getGrounded(self):
        return self.grounded

    def getPropulsion(self):
        return self.propulsion

    def setPropulsion(self, propulsion_state):
        self.propulsion = propulsion_state

    def setMass(self,dt):
        self.mass = self.mass - self.mass_flow*dt

    def actualizeAngle(self,dt):
        if self.grounded:
            self.theta = self.theta + self.Parent.w*dt
        else:
            if self.vx >= 0:
                self.theta= np.arctan(self.vx/self.vy)
            elif self.vx < 0:
                self.theta = np.arctan(self.vx/self.vy) + np.pi


    def acceleration(self, objectList):
        '''Compute the acceleration of the rocket in three cases: if it is grounded, if it not grounded and the propulsion is on and if it is not grounded and the propulsion is off'''
        #If it is grounded and the propulsion is on actualize grounded
        if self.propulsion and self.grounded:
            self.grounded = False

        #If it is grounded, pass
        if self.grounded:
            return

        #If it is not grounded compute the acceleration
        self.ax = 0
        self.ay = 0

        #Compute the gravitationnal acceleration as usual
        for celest_object in objectList.values():
            self.ax += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_object.x - self.x)/self.distance(celest_object))
            self.ay += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_object.y - self.y)/self.distance(celest_object))

        #If the propulsion is on, compute the acceleration of the propulsion
        if self.propulsion:
            self.ax += - self.mass_flow * ( -self.ejection_speed*(np.cos(self.theta)) - self.vx)
            self.ay += - self.mass_flow * ( -self.ejection_speed*(np.sin(self.theta)) - self.vy)

    def actualizeSystem(self,  dt):
        #If it is grounded make it rotate on the surface of its mother planet
        if self.grounded:
            #Define the planet the mother planet
            mother_planet = self.Parent

            #Define the initial relative position vector
            x1 = self.x - mother_planet.x
            y1 = self.y - mother_planet.y

            #Actualizing the position of the rocket
            self.x = mother_planet.x + ( x1 * np.cos(mother_planet.w * dt) - y1 * np.sin(mother_planet.w * dt) )
            self.y = mother_planet.y + ( x1 * np.sin(mother_planet.w * dt) + y1 * np.cos(mother_planet.w * dt) )

        #If it is not grounded compute as usual
        else:
            #If the system has not been initialize, do the first step with Euler method
            if not self.init:
                init = True
                #Change the speed with the acceleration using Euler method
                self.vx = self.vx + self.ax * dt
                self.vy = self.vy + self.ay * dt

                #Compute the position using the spedd and Euler's method
                x = self.x + self.vx * dt
                y = self.y + self.vy * dt

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

        #If if propulsion is on actualize mass
        if self.propulsion:
            self.setMass(dt)

        #Actualize the angle of the rocket
        self.actualizeAngle(dt)

    def collision(self,objectList):
        if not self.grounded:
            for celest_object in objectList.values():
                if self.distance(celest_object) < 0.8*(self.radius + celest_object.radius) :
                    self.collisions.append(celest_object.index)
