
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

def getPlan(count):
    #Defining constants
    dt = 1

    x=150*10**8*np.random.randn(count)
    y=150*10**8*np.random.randn(count)
    vx=10**4*np.random.randn(count)
    vy=10**4*np.random.randn(count)
    mass=4.5*10**27*np.random.randn(count)+5*10**28
    radius = [1000*(((3*m)/(density_t * 4 * np.pi))**(1/3))/150 for m in mass]
    w=1.09367*10**-5*np.random.randn(count)+7.2921159*10**-5

    soleil =  Planet(0            ,0    ,0              ,0              ,1.981*10**30              ,300*696342000 , 10)
    mercure = Planet(46001272000  ,0    ,0              ,58980          ,3.3011*10**23             ,1000*2439700  , 20)
    venus =   Planet(107476259000 ,0    ,0              ,35260          ,4.8685*10**24             ,1000*6051800  , 30)
    terre =   Planet(147098079000 ,0    ,0              ,30287          ,5.9736*10**24             ,1000*6371008  , 40)
    p=[soleil,mercure,venus,terre]
    objectList={}
    for i in range(4):
          #objectList.update({i:Planet(x[i],y[i],vx[i],vy[i],mass[i],radius[i],w[i])})
          objectList.update({i:p[i]})
    return objectList

