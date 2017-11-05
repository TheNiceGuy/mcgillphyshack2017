#!/usr/bin/env python3

#Importer les modules
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np


#Definition des planètes du système solaire
soleil =  Planet(0           ,0    ,0              ,0              ,1.981*10**30              ,30*696342000 , 10)
mercure = Planet(46001272000 ,0    ,0              ,58980          ,3.3011*10**23             ,200*2439700  , 20)
venus =   Planet(107476259000,0    ,0              ,35260          ,4.8685*10**24             ,200*6051800  , 30)
terre =   Planet(147098079000,0    ,0              ,30287          ,5.9736*10**24             ,200*6371008  , 40)
mars  =   Planet(206644545000,0    ,0              ,26499          ,641.85*10**21             ,200*3396200  , 15)

def getPlan():
    dt=1
    objectList={}
    for i,planet in zip(range(5),[soleil,mercure,venus,terre,mars]):
        objectList.update({i:planet})

    return objectList
