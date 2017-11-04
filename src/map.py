#!/usr/bin/env python3
from celestial_object import*
#from constants import*
from planet import*
#from potential import*
#from rocket import*
import numpy as np
x=150*10**6*np.random.rand(6)+10**8
y=150*10**6*np.random.rand(6)+10**8
vx=30000*np.random.rand(6)+10**3
vy=30000*np.random.rand(6)+10**3
mass=5*10**28*np.random.rand(6)+4.5*10**27
radius=6000000*np.random.rand(6)+9*10**5
w=7.2921159*10**-5*np.random.randn(6)+1.09367*10**-5
objectList={}
for i in range(0,6):
    p=Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])
    objectList.update({p.index:p})
#print('ax: {}'.format(objectList[1].ax))

#print('x: {}'.format(objectList[1].x))

for planet in objectList.values():
    planet.acceleration(objectList)
print(objectList[1].ax)
for planet in objectList.values():
    planet.actualizeSystem(2)

#print('ax: {}'.format(objectList[1].ax))

#print('x: {}'.format(objectList[1].x))
