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

class SteadyPlanet(Planet):
    def __init__(self,x,y,vx,vy,mass,radius,w):
        super().__init__(x,y,vx,vy,mass,radius,w)

    def distance(self, other_object):
        pass
    def acceleration(self,objectList,dt):
        pass
    def  actualizeSystem(self,dt):
        pass

a=SteadyPlanet(1,2,3,4,5,6,7)
a.actualizeSystem(5)
print(a.x)
