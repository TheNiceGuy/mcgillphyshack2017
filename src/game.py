#!/usr/bin/env python3

import pygame
import sys
import threading
import time

from PyQt4 import QtGui
from interface import *

class Game(object):
    def __init__(self, qtarg):
        # initialise pygame
        pygame.init();
 
        # the game is not running
        self.__running = False

        # initialise qt
        self.__app = QtGui.QApplication(qtarg)
        self.__window = MainWindow(self)

    def start(self):
        # set the game as running
        self.__running = True

        # the main thread will handle QT events
        self.__window.start()
        self.__window.show()
        self.__app.exec_()

        # set the game as not running
        self.__running = False

    def running(self):
        return self.__running

if __name__ == "__main__":
    game = Game(sys.argv)
    game.start()
    
