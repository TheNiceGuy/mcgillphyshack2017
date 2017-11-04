# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:10:16 2017

@author: utilisateur1
"""
from constants import *
from celestial_object import *
import numpy as np

class Rocket(CelestialObject):
    '''defining the rocket class that caracterizes the rocket in the simulation'''

    def __init__(self, x, y, vx, vy, mass, radius, grounded=True, Parent_index=0, qte_gas=200*1000, ejection_speed=4000, mass_flow=1000, propulsion=False):
        super().__init__(x, y, vx, vy, mass, radius)
        self.qte_gas = qte_gas
        self.ejection_speed = ejection_speed
        self.mass_flow = mass_flow

    def getGrounded(self):
        return self.grounded

    def getPropulsion(self):
        return self.propulsion

    def setPropulsion(self, propulsion_state):
        self.propulsion = propulsion_state

    def acceleration(self, objectList):
        '''Compute the acceleration of the rocket in three cases: if it is grounded, if it not grounded and the propulsion is on and if it is not grounded and the propulsion is off'''
        #If it is grounded and the propulsion is on actualize grounded
        if self.propulsion and self.grounded:
            self.grounded = False

        #If it is grounded, pass
        if self.grounded:
            pass

        #If it is not grounded compute the acceleration
        else:
            self.ax = 0
            self.ay = 0

            #Compute the gravitationnal acceleration as usual
            for celest_object in objectList.values():
                self.ax += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.x - self.x)/self.distance(celest_object))
                self.ay += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.y - self.y)/self.distance(celest_object))

            #If the propulsion is on, compute the acceleration of the propulsion
            if self.propulsion:
                self.ax += - mass_flow * ( ejection_speed * (self.vx/np.sqrt(self.vx**2 + self.vy**2)) - self.vx )
                self.ay += - mass_flow * ( ejection_speed * (self.vy/np.sqrt(self.vx**2 + self.vy**2)) - self.vy )

    def actualizeSystem(self, objectList, dt):
        #If it is grounded make it rotate on the surface of its mother planet
        if grounded:
            #Define the planet the mother planet
            mother_planet = objectList[Parent_index]

            #Define the initial relative position vector
            x1 = self.x - mother_planet.x
            y1 = self.y - mother_planet.y

            #Actualizing the position of the rocket
            self.x = mother_planet.x + ( x1 * np.cos(mother_planet.w * dt) - y1 * np.sin(mother_planet.w * dt) )
            self.y = mother_planet.y + ( x1 * np.sin(mother_planet.w * dt) + y1 * np.cos(mother_planet.w * dt) )

        #If it is not grounded compute as usual
        else:



