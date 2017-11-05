from celestial_object import *
from rocket import *
from constants import *
from planet import *
from potential import *
import numpy as np


def getPlan(count):
    #Defining constants
    x=150*10**8*np.random.randn(count)
    y=150*10**8*np.random.randn(count)
    vx=10**4*np.random.randn(count)
    vy=10**4*np.random.randn(count)
    mass=4.5*10**27*np.random.randn(count)+5*10**28
    radius = [1000*(((3*m)/(density_t * 4 * np.pi))**(1/3))/150 for m in mass]
    w=1.09367*10**-5*np.random.randn(count)+7.2921159*10**-5

    objectList={}
    for i in range(count):
        objectList.update({i:Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])})

    rock=Rocket(2700*1000,10**8,3,objectList[3],0,0)
    return objectList,rock

