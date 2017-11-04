#!/usr/bin/env python3

import pygame
import sys

from interface import *

if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    # create the application
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    # run the application
    window.start()
    window.show()
    app.exec_()
