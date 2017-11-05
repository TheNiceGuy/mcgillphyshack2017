#!/usr/bin/env python3

import sys
import threading
import time

from PyQt4 import QtGui
from interface import *
#from liste_plan import *
from systeme_solaire import *
from map import *


class Game(object):
    def __init__(self):
        self.__running = False
        self.__map = Map(getPlan(8))

    def start(self):
        # set the game as running
        self.__running = True

    def stop(self):
        # set the game as not running
        self.__running = False

    def setPropulsion(self, state):
        pass

    def running(self):
        return self.__running

    def getMap(self):
        return self.__map

if __name__ == "__main__":
    game = Game(sys.argv)
    game.start()

