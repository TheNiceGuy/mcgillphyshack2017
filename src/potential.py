#!/usr/bin/env python3
"""
Created on Sat Nov  4 10:10:48 2017

@author: utilisateur1
"""
import numpy, time, math
import matplotlib # for changing the matplotlib.contour behavior
import matplotlib.pyplot as plt
from constants import *
    
    
# defining a function that compute the distance between a celestial object (from that class) and a point
"""Definition________________________________________________"""
def distanceCompute(celestialObject, position_x, position_y):
    delta_x = celestialObject.x-position_x
    delta_y = celestialObject.y-position_y
    #print(delta_x**2,delta_y**2)
    distance = numpy.sqrt(delta_x**2 + delta_y**2)
    return distance
"""__________________________________________________________________"""

class TestCelestialObject(object):
    def __init__(self, x,y,m):
        self.x=x
        self.y=y
        self.m=m

class Potential(object):
    def __init__(self, delta):
        self.delta = delta
        
    def compute(self, objectList, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x_list = numpy.arange(x_min-self.delta, x_max+self.delta, self.delta)
        self.y_list = numpy.arange(y_min-self.delta, y_max+self.delta, self.delta)
        
        self.potentialMatrix = numpy.zeros( (len(self.y_list), len(self.x_list)) )
        
        # for each point on the discretization of space: (double for)
        for iterate_x in range(len(self.x_list)) :
            position_x = self.x_list[iterate_x]
            for iterate_y in range(len(self.y_list)) :
                position_y = self.y_list[iterate_y]
                # adding the potential from each celestial object contained in objectList
                for i in objectList.keys():
                    distance_i = distanceCompute(objectList[i], position_x, position_y)
                    if distance_i ==0:
                        self.potentialMatrix[-iterate_y, iterate_x] = self.potentialMatrix[-iterate_y+1, iterate_x-1]
                    else:
                        addPotential = -(G/(distance_i))*(objectList[i].mass)
                        self.potentialMatrix[-iterate_y, iterate_x] = self.potentialMatrix[-iterate_y, iterate_x] + addPotential
        
    def initialisePlot(self, potentialFigure):
        # we now define the plot for the potential with matplotlib
        self.potentialFigure = potentialFigure
        self.potentialFigure.ax = potentialFigure.add_subplot(1,1,1)
        
        matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
        self.coloring =  self.potentialFigure.ax.imshow( self.potentialMatrix, interpolation='bilinear', cmap='spectral', extent= [self.y_min, self.y_max, self.x_min, self.x_max], animated=True)     
        #self.lines = self.potentialFigure.ax.contour(self.potentialMatrix, linewidths=1, colors='k', extent= [self.x_min, self.x_max, self.y_min, self.y_max], animated=True)
        self.colorbar = plt.colorbar(self.coloring, shrink=0.8, extend='both')
        
        self.potentialFigure.ax.set_xlabel("x (m)")
        self.potentialFigure.ax.set_ylabel("y (m)")
        plt.title("Gravitationnal potential (J/kg)")
        
    def actualisePlot(self, potentialFigure):
        # actualise the plot
        #self.lines.set_data(self.potentialMatrix)
        self.potentialFigure = potentialFigure
        self.potentialFigure.ax = potentialFigure.add_subplot(1,1,1)
        
        matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
        self.coloring =  self.potentialFigure.ax.imshow( self.potentialMatrix, interpolation='bilinear', cmap='spectral', extent= [self.y_min, self.y_max, self.x_min, self.x_max], animated=True)     
#        self.potentialFigure.canvas.draw()
        
            
if __name__ == "__main__":
    main()
        
    
        
