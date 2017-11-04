# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:10:16 2017

@author: utilisateur1
"""
from constants import *
from celestial_object import *

class Rocket(CelestialObject):
    '''defining the rocket class that caracterizes the rocket in the simulation'''

    def __init__(self, x, y, vx, vy, mass, radius, qte_gas=200*1000, ejection_speed=4000, mass_flow=1000, grounded=True, propulsion=False):
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
        #If it is grounded and the propulsion is True actualize grounded
        if self.propulsion and self.grounded:
            self.grounded = False

        #If it is grounded, pass
        if self.grounded:
            pass

        #If it is not grounded compute the acceleration
        else:
            self.ax = 0
            self.ay = 0
            #If the propulsion is not on do as usual
            if not self.propulsion:
                for celest_object in objectList:
                    self.ax += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.x - self.x)/self.distance(celest_object))
                    self.ay += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.y - self.y)/self.distance(celest_object))

            #If the propulsion is on, compute the gravitationnal acceleration and the acceleration of the propulsion
            elif self.propulsion:
                for celest_object in objectList:
                    ax += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.x - self.x)/self.distance(celest_object))
                    ay += ((G * celest_object.mass)/self.distance(celest_object)**2) * ((celest_objects.y - self.y)/self.distance(celest_object))



    def actualizeSystem(self, ):
        if grounded:


        else:

