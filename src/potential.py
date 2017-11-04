#!/usr/bin/env python3
"""
Created on Sat Nov  4 10:10:48 2017

@author: utilisateur1
"""
import math, numpy
import matplotlib.pyplot as plt
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
        
        self.x_plot,self.y_plot = numpy.meshgrid(self.x_list, self.y_list)
        
        # initialising a matrix (numpy) containing the potential in each point of the discretization of space      
        self.potentialMatrix = numpy.zeros( (len(self.x_list),len(self.y_list)) )
    
    
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
    
    def initialisePlot(self, potentialFigure):
        # we now define the plot for the potential with matplotlib
        self.potentialFigure = potentialFigure
        self.potentialFigure.ax = potentialFigure.add_subplot(1, 1,1)
        #self.potentialFigure.ax.contour(self.x_plot, self.y_plot, self.potentialMatrix)
        
        Z=10.0 * (self.x_plot-self.y_plot)
        self.potentialFigure.ax.contour(self.x_plot, self.y_plot, self.potentialMatrix, colors='k')
        self.potentialFigure.ax.imshow(self.potentialMatrix, interpolation='bilinear', cmap='spectral')        
        self.potentialFigure.ax.set_xlabel("x (m)")
        self.potentialFigure.ax.set_ylabel("y (m)")
        #self.potentialFigure.ax.set_zlabel("U (J/kg)")
        #plt.show()
        
    def actualisePlot(self):
        # actualise the plot
        #potentialFigure.ax.set_data(self.potentialMatrix)
        plt.show()
        
        
            
if __name__ == "__main__":
    planetTest = TestCelestialObject(5000*10**(4),5000*10**(4),2*10**(30))
    planetTest2 = TestCelestialObject(7000*10**(4),6000*10**(4),4*10**(30))
    planetTest3 = TestCelestialObject(10000*10**(4),15000*10**(4),3.5*10**(30))    
    planetTest3 = TestCelestialObject(15000*10**(4),15000*10**(4),2*10**(30))   
    planetTest4 = TestCelestialObject(6000*10**(4),12000*10**(4),7*10**(30))   
    planetTest5 = TestCelestialObject(4000*10**(4),16000*10**(4),4.3*10**(30))
    planetTest6 = TestCelestialObject(14000*10**(4),7000*10**(4),1.5*10**(30))       
    objectList=[]
    objectList.append(planetTest)
    objectList.append(planetTest2)    
    objectList.append(planetTest3)    
    objectList.append(planetTest4)
    objectList.append(planetTest5)
    objectList.append(planetTest6)
    
    potential = Potential(2.0*10**(8), 6000.0*10**(3))
    potentialFigure = plt.figure('3d view')
    potential.compute(objectList)
    potential.initialisePlot(potentialFigure)
    potential.actualisePlot()
