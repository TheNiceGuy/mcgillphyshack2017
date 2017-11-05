#!/usr/bin/env python3

import sys
import threading
import time

from PyQt4 import QtGui
from interface import *
from liste_plan import *
#from systeme_solaire import *
#from system_moons import *

from map import *


class Game(object):
    def __init__(self):
        self.__running = False
        o,r=getPlan(10)
        self.__map = Map(o,r)

    def start(self):
        # set the game as running
        self.__running = True

    def stop(self):
        # set the game as not running
        self.__running = False

    def setPropulsion(self, state):
        rocket = self.__map.getRocket()
        if rocket is None:
            return;

        rocket.setPropulsion(state)

    def running(self):
        return self.__running

    def getMap(self):
        return self.__map

if __name__ == "__main__":
    game = Game(sys.argv)
    game.start()

