#!/usr/bin/env python3
"""
Created on Sat Nov  4 10:10:48 2017

@author: utilisateur1
"""
import matplotlib, math, numpy
from mpl_toolkits.mplot3d import Axes3D

from constants import *


# defining a function that compute the distance between a celestial object (from that class) and a point
"""Definition________________________________________________"""
def distanceCompute(celestialObject, position_x, position_y):
    delta_x = celestialObject.x-position_x
    delta_y = celestialObject.y-position_y
    distance = math.sqrt(delta_x**2 + delta_y**2)
    return distance
"""__________________________________________________________________"""

class TestCelestialObject(object):
    def __init__(self, x,y,m):
        self.x=x
        self.y=y
        self.m=m

class Potential(object):
    def __init__(self, size, delta):
        # defining the side size of the 2D square region studied (in meters)
        self.size = size
        # step size in position for the computing of the potential
        self.delta = delta
        # lists of x and y positions
        self.x_list = numpy.arange(0.0, self.size + self.delta, self.delta)
        self.y_list = numpy.arange(0.0, self.size + self.delta, self.delta)
        
        # initialising a matrix (numpy) containing the potential in each point of the discretization of space      
        self.potentialMatrix = numpy.matrix( numpy.zeros( (len(self.x_list),len(self.y_list)) ))
    
    
    def compute(self, objectList):
        
        # for each point on the discretization of space: (double for)
        for iterate_x in range(0,len(self.x_list)) :
            position_x = self.x_list[iterate_x]
            for iterate_y in range(0,len(self.y_list)) :
                position_y = self.y_list[iterate_y]
                # adding the potential from each celestial object contained in objectList
                for i in range(0, len(objectList)):
                    distance_i = distanceCompute(objectList[i], position_x, position_y)
                    if distance_i ==0:
                        self.potentialMatrix[iterate_x, iterate_y] = self.potentialMatrix[iterate_x-1, iterate_y-1]
                    else:
                        addPotential = -(G/(distance_i))*(objectList[i].m)
                        self.potentialMatrix[iterate_x, iterate_y] = self.potentialMatrix[iterate_x, iterate_y] + addPotential
                        
        # we now plot the potential with matplotlib
        potentialFigure = matplotlib.pyplot.figure()
        ax = potentialFigure.add_subplot(111, projection='3d')
        potentialPlot = ax.plot_surface(self.x_list, self.y_list, self.potentialMatrix, rstride=1, cstride=1, shade=False, cmap="spectral", linewidth=0)
        #potentialFigure.show()
            
if __name__ == "__main__":
    planetTest = TestCelestialObject(5000*10**(4),5000*10**(4),2*10**(30))
    planetTest2 = TestCelestialObject(7000*10**(4),6000*10**(4),4*10**(30))
    planetTest3 = TestCelestialObject(10000*10**(4),15000*10**(4),6*10**(30))    
    objectList=[]
    objectList.append(planetTest)
    objectList.append(planetTest2)    
    objectList.append(planetTest3)    
    
    potential = Potential(2.0*10**(8), 6000.0*10**(3))
    potential.compute(objectList)
