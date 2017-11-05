#!/usr/bin/env python3

#Importer les modules
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np


#Definition des planètes du système solaire
soleil =  Planet(0           ,0    ,0              ,0              ,1.981*10**30              ,30*696342000, 10)
mercure = Planet(46001272000 ,0    ,0              ,58980          ,3.3011*10**23             ,200*2439700  , 10)
venus =   Planet(107476259000,0    ,0              ,35260          ,4.8685*10**24             ,200*6051800  , 10)


def getPlan():
    dt=1
    objectList={}
    for i,planet in zip(range(3),[soleil,mercure,venus]):
        objectList.update({i:planet})

    return objectList


