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

    def collide(self,other_planet):
        #Update the data of the  planet:
        # The radius
        self.radius = (self.radius**3 + other_planet.radius**3)**(1/3)

        # The speed
        self.vx  = (self.mass * objectList[i].vx + objectList[j].mass * objectList[j].vx)/(objectList[j].mass + objectList[i].mass)
        self.vy  = (self.mass * objectList[i].vy + objectList[j].mass * objectList[j].vy)/(objectList[j].mass + objectList[i].mass)

        # The position
        self.x = (self.mass*self.x + other_planet.mass*other_planet.x)/(self.mass + other_planet.mass)
        self.y = (self.mass*self.y + other_planet.mass*other_planet.y)/(self.mass + other_planet.mass)

        # The mass
        self.mass = self.mass + other_planet.mass

        # Other parameters of initialisation
        self.x0 = 0
        self.y0 = 0
        self.ax = 0
        self.ay = 0
        self.collision = []
        self.w = (self.w + other_planet.w)/2
        self.init = False

class SteadyPlanet(Planet):
    def __init__(self,x,y,vx,vy,mass,radius,w):
        super().__init__(x,y,vx,vy,mass,radius,w)

    def distance(self, other_object):
        pass
    def acceleration(self,objectList,dt):
        pass
    def  actualizeSystem(self,dt):
        pass
