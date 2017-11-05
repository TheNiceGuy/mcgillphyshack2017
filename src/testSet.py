from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np
import matplotlib.pyplot as plt

def getPlan():
        #Defining constants
    dt = 1
    x=150*10**8*np.random.randn(20)
    y=150*10**8*np.random.randn(20)
    vx=10**3*np.random.randn(20)+30000
    vy=10**3*np.random.randn(20)+30000
    mass=4.5*10**27*np.random.randn(20)+5*10**28
    radius = [(((3*m)/(density_t * 4 * np.pi))**(1/3))/150 for m in mass]
    w=1.09367*10**-5*np.random.randn(20)+7.2921159*10**-5

    objectList={}
    for i in range(0,20):
        objectList.update({i:Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])})
        return objectList

p=getPlan()
pos_x=[]
pos_y=[]
area=[]
for planet in p.values():
    pos_x.append(planet.x)
    pos_y.append(planet.y)
    area.append(np.pi*planet.radius)



colors = np.random.rand(len(pos_x))

plt.scatter(pos_x, pos_y,c=colors, s=area, alpha=0.5)
plt.show()
