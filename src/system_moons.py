# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 08:52:06 2017

@author: utilisateur1
"""
#Importer les modules
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np
import math
import time

objectList={}
#Definition des planètes du système solaire
objectList.update({0:Planet(0            ,0    ,0              ,0              ,1.5*10**24              ,500*10**6 , 10*10**7)})
objectList.update({1:Planet( 4*10**9*math.cos(math.pi/4)      ,4*10**9*math.sin(math.pi/4)    ,1000*math.cos(math.pi/4)              ,1000*math.sin(math.pi/4)          ,1,5*10**22              ,0.1*2*10**6  , 2*10**7)})
objectList.update({2:Planet( 5*10**9*math.cos(math.pi/6)      ,5*10**9*math.sin(math.pi/6)    ,1200*math.cos(math.pi/6)              ,1200*math.sin(math.pi/6)          ,1,6*10**22              ,0.1*2.3*10**6  , 1*10**7)})
objectList.update({3:Planet( 7*10**9*math.cos(math.pi/2)      ,7*10**9*math.sin(math.pi/2)    ,1500*math.cos(math.pi/2)              ,1500*math.sin(math.pi/2)          ,1,2*10**21              ,0.1*1.7*10**6  , 5*10**7)})
objectList.update({4:Planet( 7.2*10**6    ,0    ,0              ,1550         ,1.8*10**21              ,1.8*10**6 , 12*10**7)})

def getPlan(count):
    
    rock=rock=Rocket(2700*1000,10**10,0,objectList[0],0,0)
    return objectList,rock
    print(objectList)
    time.sleep(20)