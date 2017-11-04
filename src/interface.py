#!/usr/bin/env python3

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *

from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

#debugging
import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6')

# System dependent, see e.g. /usr/include/x86_64-linux-gnu/asm/unistd_64.h
SYS_gettid = 186

'''
mainView
* splitterGameView
  * gameView
  * splitterLevelView
    * levelView
    * controlsView
'''

class MainWindow(QWidget):
    def __init__(self, game, parent=None):
        super(MainWindow,self).__init__(parent)

        self.__game = game

        # controls of the application
        self.__controlsView = QFrame()
        self.__controlsView.setFrameShape(QFrame.StyledPanel)

        self.__levelView = PlotWidget(self)

        # splitter for the controls view and the level view
        self.__splitterLevelView = QSplitter(Qt.Vertical)
        self.__splitterLevelView.addWidget(self.__controlsView)
        self.__splitterLevelView.addWidget(self.__levelView)

        # opengl drawing
        self.__gameView = GLWidget(game)

        # splitter for the game view and the level splitter
        self.__splitterGameView = QSplitter(Qt.Horizontal)
        self.__splitterGameView.addWidget(self.__gameView)
        self.__splitterGameView.addWidget(self.__splitterLevelView)

        # main view
        self.__mainView = QHBoxLayout(self)
        self.__mainView.addWidget(self.__splitterGameView)

        self.setLayout(self.__mainView)

        self.__tickThread = TickThread(game, self)
        self.connect(self.__tickThread, self.__tickThread.getSignal(), self.updateTick)

    def start(self):
        self.__tickThread.start()

    def updateTick(self):
        print("map updated")
        self.__gameView.update()
        #self.__levelView.update()

    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()

    def keyPressEvent(self, event):
        pass

    def redraw(self, gamemap):
        self.__gameView.redraw(gamemap)

class TickThread(QThread):
    def __init__(self, game, parent=None):
        QThread.__init__(self, parent)

        self.__signal = SIGNAL("tick")
        self.__game = game

    def run(self):
        print("Tick thread starting")

        while(self.__game.running()):
            self.emit(self.__signal, None)
            time.sleep(1)

        print("tick thread ending")

    def getSignal(self):
        return self.__signal
        

class GLWidget(QGLWidget):
    def __init__(self, game, parent=None):
        QGLWidget.__init__(self, parent)

        self.__game = game
        self.__temp = 0

    def resizeEvent(self, event):
        # get the new size of the widget
        width = event.size().width()
        height = event.size().height()

        # resize the GL viewport
        glViewport(0, 0, width, height)

    def paintGL(self):
        gamemap = [(1,1),(2,2)]

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()


        glTranslatef(-2.5, 0.5, -6.0)
        glColor3f( 1.0, 1.5, 0.0 );
        glPolygonMode(GL_FRONT, GL_FILL);

        self.__temp += 0.05

        glBegin(GL_TRIANGLES)
        glVertex3f(self.__temp,-1.2,0.0)
        glVertex3f(2.6,0.0,0.0)
        glVertex3f(2.9,-1.2,0.0)
        glEnd()


        glFlush()
        return

        print("redraw")
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        for (x,y) in gamemap:
            glBegin(GL_TRIANGLES)
            glColor(0,0,1,1)
            glVertex3f(x  , y  , 0.0)
            glVertex3f(x+1, y  , 0.0)
            glVertex3f(x+1, y+1, 0.0)
            glEnd()           
        glFlush()

    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0,1.33,0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

class PlotWidget(FigureCanvasQTAgg):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)

        FigureCanvasQTAgg.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

    def compute_initial_figure(self):
        pass
