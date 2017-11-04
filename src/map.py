#!/usr/bin/env python3

#Importing packages
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

#Defining constants
dt = 1
x=150*10**6*np.random.rand(6)+10**8
y=150*10**6*np.random.rand(6)+10**8
vx=30000*np.random.rand(6)+10**3
vy=30000*np.random.rand(6)+10**3
mass=5*10**28*np.random.rand(6)+4.5*10**27
radius = [(((3*m)/(densitee_terre * 4 * np.pi))**(1/3))/150 for m in mass]
w=7.2921159*10**-5*np.random.randn(6)+1.09367*10**-5

#Constructing the objectList dictionnary
objectList={}
for i in range(CelestialObject.count):
    objectList.update({i:Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])})

def Step():
    #Update the acceleration for all objects
    for planet in objectList.values():
        planet.acceleration(objectList)

    #Update the data of all the objects
    for planet in objectList.values():
        planet.actualizeSystem(dt)


