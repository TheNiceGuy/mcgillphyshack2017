
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

def getPlan():
    #Defining constants
    dt = 1
    x=150*10**6*np.random.rand(6)+10**8
    y=150*10**6*np.random.rand(6)+10**8
    vx=30000*np.random.rand(6)+10**3
    vy=30000*np.random.rand(6)+10**3
    mass=5*10**28*np.random.rand(6)+4.5*10**27
    radius = [(((3*m)/(density_t * 4 * np.pi))**(1/3))/150 for m in mass]
    w=7.2921159*10**-5*np.random.randn(6)+1.09367*10**-5

    objectList={}
    for i in range(0,6):
          objectList.update({i:Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])})

    return objectList

