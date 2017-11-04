#!/usr/bin/env python3
from celestial_object import*
from constants import*

class Planet(CelestialObject):
    def __init__(self,x,y,vx,vy,mass,radius,w,angle=0):
        super().__init__(x,y,vx,vy,mass,radius)
        self.w=w
        self.angle=angle

    def actualizeAngle(self,dt):
        self.angle=self.w*dt+self.angle

    def getAngle(self):
        return self.angle
