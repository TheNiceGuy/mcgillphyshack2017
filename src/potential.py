# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:10:48 2017

@author: utilisateur1
"""

import matplotlib
import numpy

from constants import *
import pygame
import pyqt4a
import pysdl2

import math

# creating a function to define a decimal linear space
"""Definition_________________________________________________________"""
def linspace(debut, fin, pas):
    #on cre la liste
    liste = []
    # on ajoute la premiere valeur
    liste.append(debut)
    # tant que le dernier nombre de la liste est inferieur à la fin, on ajoute un autre nombre à la liste selon le pas specifie
    while liste[-1] < fin :
        liste.append(liste[-1]+pas)
    
    # si la deniere valeur est > fin, on la supprime
    if liste[-1]>fin:
        del(liste[-1])
        
    # la liste est finie et est retournee
    return liste
"""____________________________________________________________________"""

# defining a function that compute the distance between a celestial object (from that class) and a point
"""Definition________________________________________________"""
def distanceCompute(celestialObject, position_x, position_y):
    delta_x = celestialObject.x-position_x
    delta_y = celestialObject.y-position_y
    distance = sqrt(delta_x**2 + delta_y**2)
"""__________________________________________________________________"""



#defining the side size of the 2D square region studied (in meters)
size = 1.0*10**(9)
# step size in posiiton for the computing of the potential
delta = 100.0*10**(3)

# defining the list of point discretization in x and y
list_y = linspace( 0, size, delta)

#creating a matrix (numpy) containing the potential in each point of the discretization of space
Potential = numpy.matrix( numpy.zeros( (size,size) )

#for each point on the discretization of space: (double for)
for position_x in numpy.arange(0, size + delta, delta):
    for position_y in numpy.arange(0, size + delta, delta) :
        # adding the potential from each celestial object contained in objectList
            for i in range(1, length(objectList)):
                distance = distanceCompute(objectList[i], position_x, position_y)
                contribution_i = 
            Potential (position_x, position_y) = Potential (position_x, position_y) + potential_i