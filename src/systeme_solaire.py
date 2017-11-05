#Importer les modules
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

objectList={}
#Definition des planètes du système solaire
objectList.update({0:Planet(0            ,0    ,0              ,0              ,1.981*10**30              ,50*696342000 , 10**-7)})
objectList.update({1:Planet(46001272000  ,0    ,0              ,58980          ,3.3011*10**23             ,200*2439700  , 20*10**-7,path1='pictures/planete3.png')})
objectList.update({2:Planet(107476259000 ,0    ,0              ,35260          ,4.8685*10**24             ,200*6051800  , 30*10**-7,path1='pictures/planete2.png')})
objectList.update({3:Planet(147098079000 ,0    ,0              ,30287          ,5.9736*10**24             ,200*6371008  , 40*10**-7)})
objectList.update({4:Planet(206644545000 ,0    ,0              ,26499          ,641.85*10**21             ,200*3389500  , 15*10**-7)})
#objectList.update({5:Planet(740520000000 ,0    ,0              ,13720          ,1.8986*10**27             ,1000*69911000 , 12)})
#objectList.update({6:Planet(2734998229000,0    ,0              ,7128           ,8.681 *10**25             ,1000*2559000  , 18)})
#objectList.update({7:Planet(4452940833000,0    ,0              ,5479           ,102.43*10**24             ,1000*2462200  , 76)})

def getPlan(count):
    rock=Rocket(2700*1000,10**10,0,objectList[3],0,0)
    return objectList,rock
    print(objectList)
    time.sleep(2)
