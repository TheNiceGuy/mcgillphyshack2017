<<<<<<< HEAD
=======


>>>>>>> 73d76a4aced43eedc9bb8ceaca3005fe7a3b7b9e
#Importer les modules
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

objectList={}
#Definition des planètes du système solaire
<<<<<<< HEAD
soleil =  Planet(0            ,0    ,0              ,0              ,1.981*10**30              ,50*696342000 , 10)
mercure = Planet(46001272000  ,0    ,0              ,58980          ,3.3011*10**23             ,200*2439700  , 20)
venus =   Planet(107476259000 ,0    ,0              ,35260          ,4.8685*10**24             ,200*6051800  , 30)
terre =   Planet(147098079000 ,0    ,0              ,30287          ,5.9736*10**24             ,200*6371008  , 40)
=======
objectList.update({0:Planet(0            ,0    ,0              ,0              ,1.981*10**30              ,300*696342000 , 10)})
objectList.update({1:Planet(46001272000  ,0    ,0              ,58980          ,3.3011*10**23             ,1000*2439700  , 20)})
objectList.update({2:Planet(107476259000 ,0    ,0              ,35260          ,4.8685*10**24             ,1000*6051800  , 30)})
objectList.update({3:Planet(147098079000 ,0    ,0              ,30287          ,5.9736*10**24             ,1000*6371008  , 40)})
>>>>>>> 73d76a4aced43eedc9bb8ceaca3005fe7a3b7b9e
#mars  =   Planet(206644545000 ,0    ,0              ,26499          ,641.85*10**21             ,1000*3396200  , 15)
#jupiter = Planet(740520000000 ,0    ,0              ,13720          ,1.8986*10**27             ,1000*69911000 , 12)
#uranus  = Planet(2734998229000,0    ,0              ,7128           ,8.681 *10**25             ,1000*2559000  , 18)
#neptune = Planet(4452940833000,0    ,0              ,5479           ,102.43*10**24             ,1000*2462200  , 76)


def getPlan(count):
<<<<<<< HEAD
    dt=1
    objectList={}
    for i,planet in zip(range(4),[soleil,mercure,venus,terre]):#,mars,jupiter,uranus,neptune]):
        print("allo")
        objectList.update({i:planet})
=======
#    objectList={}
#    for i,planet in zip(range(4),[soleil,mercure,venus,terre]):#,mars,jupiter,uranus,neptune]):
#        print("allo")        
#        objectList.update({i:planet})
>>>>>>> 73d76a4aced43eedc9bb8ceaca3005fe7a3b7b9e
    print(objectList)
    return objectList
