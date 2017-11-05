#!/usr/bin/env python3

import sys

from interface import *

if __name__ == "__main__":
    # create the application
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    # run the application
    window.start()
    window.show()
    app.exec_()
