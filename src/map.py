#!/usr/bin/env python3

#Importing packages
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

#Defining constants
dt = 800

class Map():
    def __init__(self, objectList, rocket=None):
        self.objectList = objectList
        print(self.objectList)
        self.rocket = rocket

        self.xlims = (0,0)
        self.ylims = (0,0)


        self.xlims  = self.getLimitsX()
        self.ylims  = self.getLimitsY()

    def getRocket():
        return self.rocket

    def getList(self):
        return self.objectList

    def getRocket(self):
        return self.rocket

    def getLimitsX(self):
        (xmin,xmax) = self.xlims

        mn = min([space_object.x for space_object in self.objectList.values()])
        mx = max([space_object.x for space_object in self.objectList.values()])

        if xmin == 0 and xmax == 0:
            return (mn,mx)
        return (xmin,xmax)

        if xmin > mn:
            mn = xmin

        if xmax < mx:
            mx = xmax

        return (mn,mx)

    def getLimitsY(self):
        (ymin,ymax) = self.ylims

        mn = min([space_object.y for space_object in self.objectList.values()])
        mx = max([space_object.y for space_object in self.objectList.values()])

        if ymin == 0 and ymax == 0:
            return (mn,mx)
        return (ymin,ymax)

        if ymin > mn:
            mn = ymin

        if ymax < mx:
            mx = ymax

        return (mn,mx)

    def Step(self):
        ###########################
        #Updating all acceleration:
        # 1) for all planets
        for objetSpatial in self.objectList.values():
            objetSpatial.acceleration(self.objectList)
        # 2) for the rocket
        if self.rocket:
            self.rocket.acceleration(self.objectList)

        ###################################
        #Update the data of all the objects
        # 1) For the planets
        for objetSpatial in self.objectList.values():
            objetSpatial.actualizeSystem(dt)
            objetSpatial.actualizeAngle(dt)
        # 2) For the rocket
        if self.rocket:
            self.rocket.actualizeSystem(dt)

        ###############################
        #Look if there is any collision
        # 1) For the planets
        for objectSpatial in self.objectList.values():
            objectSpatial.collision(self.objectList)
        # 2) for the rocket
        if self.rocket is not None:
            self.rocket.collision(self.objectList)

        ########################
        #Deal with the collision
        # 1) For the planets
        # i) Construct a list of all the tuple of the planets that collided
        index_collision = []
        for objectSpatial in self.objectList.values():
            if not objectSpatial.collisions:
                continue

            for index_col in objectSpatial.collisions:
                if (objectSpatial.index, index_col) in index_collision:
                    continue

                if (index_col, objectSpatial.index) in index_collision:
                    continue

                index_collision.append((objectSpatial.index, index_col))

        for planet in self.objectList.values():
            planet.collisions = []

        # ii) For all the collided planet define a new one and erase the collided ones
        if index_collision:
            for i,j in index_collision:
                self.objectList[i].collide(self.objectList[j])
                del self.objectList[j]

        # 2) For the rocket
        if self.rocket:
            if self.rocket.collisions:
                print('entered')
                return True


