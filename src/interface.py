#!/usr/bin/env python3

import sys
import time
import math

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

from game import *

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
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.__game = Game()

        # fuel gauge
        self.__fuelGauge = QProgressBar()
        self.__fuelGauge.setOrientation(Qt.Vertical)


        # controls of the application
        self.__splitterControls = QSplitter(Qt.Horizontal)
        self.__splitterControls.addWidget(self.__fuelGauge)
        self.__splitterControls.addWidget(QFrame())

        # plot view
        self.__levelView = PlotWidget(self)

        # splitter for the controls view and the level view
        self.__splitterLevelView = QSplitter(Qt.Vertical)
        self.__splitterLevelView.addWidget(self.__splitterControls)
        self.__splitterLevelView.addWidget(self.__levelView)

        # opengl drawing
        self.__gameView = GLWidget(self.__game.getMap())

        # splitter for the game view and the level splitter
        self.__splitterGameView = QSplitter(Qt.Horizontal)
        self.__splitterGameView.addWidget(self.__gameView)
        self.__splitterGameView.addWidget(self.__splitterLevelView)

        # main view
        self.__mainView = QHBoxLayout(self)
        self.__mainView.addWidget(self.__splitterGameView)
        self.setLayout(self.__mainView)

        # create the updating thread
        self.__tickThread = TickThread(self.__game, self)
        self.connect(self.__tickThread, self.__tickThread.getSignal(), self.updateTick)

    def start(self):
        self.__game.start()
        self.__tickThread.start()

    def stop(self):
        self.__game.stop()

    def updateTick(self):
        print("map updated")
        self.__gameView.update()
        self.__game.getMap().Step()
        #self.__levelView.update()

    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()

    def keyPressEvent(self, event):
        # propulse the rocket
        if event.key() == Qt.Key_Space:
            self.__game.setPropulsion(True)

    def keyReleaseEvent(self, event):
        # stop the rocket propulsion
        if event.key() == Qt.Key_Space:
            self.__game.setPropulsion(False)

    def closeEvent(self, event):
        self.__game.stop()
        self.__tickThread.wait()

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
            time.sleep(1.0/60)

        print("tick thread ending")

    def getSignal(self):
        return self.__signal
        

class GLWidget(QGLWidget):
    def __init__(self, gamemap, parent=None):
        QGLWidget.__init__(self, parent)

        self.__map = gamemap
        self.__width = 0
        self.__height = 0

    def resizeEvent(self, event):
        # get the new size of the widget
        self.__width = event.size().width()
        self.__height = event.size().height()

        # resize the GL viewport
        glViewport(0, 0, self.__width, self.__height)

    def mousePressEvent(self, event):
        print(event.x(), event.y())

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        (minx,maxx) = self.__map.getLimitsX()
        (miny,maxy) = self.__map.getLimitsY()

        width  = maxx-minx
        height = maxy-miny

        dx = 0
        dy = 0


        glClearColor(0, 0.3, 0, 1);

        if width < height:
            dx = math.floor(height*(self.__width/self.__height)-width)
        else:
            dy = math.floor(width*(self.__height/self.__width)-height)
    
        minx -= dx/2
        maxx += dx/2
        miny -= dy/2
        maxy += dy/2

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(minx, maxx, miny, maxy, 0.0001, 100000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor3f( 1.0, 1.5, 0.0 );
        glPolygonMode(GL_FRONT, GL_FILL);

        # draw the planets
        for planet in self.__map.getList().values():
            x = planet.getX()
            y = planet.getY()
            r = planet.getRadius()

            glCircle(x, y, 1000*r)

        # TODO: draw the rocket

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

def glCircle(px, py, r):
    count = 20
    angle = 2*math.pi/count

    glBegin(GL_TRIANGLES)
    for i in range(count):
        px1 = px+r*math.cos((i+0)*angle)
        py1 = py+r*math.sin((i+0)*angle)

        px2 = px+r*math.cos((i+1)*angle)
        py2 = py+r*math.sin((i+1)*angle)

        glVertex3f(px,  py,  0.0)
        glVertex3f(px1, py1, 0.0)
        glVertex3f(px2, py2, 0.0)
    glEnd()


class PlotWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # initialise the figure
        self.__figure = Figure()
        self.__figure.patch.set_facecolor("None")

        # we want a transparent background
        self.axes = self.__figure.add_subplot(111)
        self.axes.patch.set_alpha(1)

        # we need minimal figure
        self.compute_initial_figure()

        # initialise this widget
        FigureCanvasQTAgg.__init__(self, self.__figure)
        self.setParent(parent)

        # configure this widget
        FigureCanvasQTAgg.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

        # transparent background
        self.setStyleSheet("background-color:transparent;")

    def compute_initial_figure(self):
        pass

