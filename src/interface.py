#!/usr/bin/env python3

import sys
import time
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PIL import Image

from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

from game import *
from potential import *

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

        # create the potential thing
        (xmin,xmax) = self.__game.getMap().getLimitsX()
        (ymin,ymax) = self.__game.getMap().getLimitsY()

        dx = xmax-xmin
        dy = ymax-ymin

        dd = (dx+dy)/2

        self.__potential = Potential(dd/20)

        # plot view
 #       self.__levelView = PlotWidget(self.__potential, self.__game.getMap(), self)
        self.__figure = Figure()
        self.__canvas = FigureCanvasQTAgg(self.__figure)

        # splitter for the controls view and the level view
        self.__splitterLevelView = QSplitter(Qt.Vertical)
        self.__splitterLevelView.addWidget(self.__splitterControls)
        self.__splitterLevelView.addWidget(self.__canvas)

        (minx,maxx) = self.__game.getMap().getLimitsX()
        (miny,maxy) = self.__game.getMap().getLimitsY()

        width  = maxx-minx
        height = maxy-miny

        w = self.frameGeometry().width()
        h = self.frameGeometry().height()

        dx = 0
        dy = 0

        if width < height:
            dx = math.floor(height*(w/h)-width)
        else:
            dy = math.floor(width*(h/w)-height)
    
        minx -= dx/2
        maxx += dx/2
        miny -= dy/2
        maxy += dy/2

        self.__potential.compute(self.__game.getMap().getList(), minx, maxx, miny, maxy)
        self.__potential.initialisePlot(self.__figure)

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

        self.__count = 0

    def start(self):
        self.__game.start()
        self.__tickThread.start()

    def stop(self):
        self.__game.stop()

    def updateTick(self):
        self.__game.getMap().Step()
        self.__gameView.update()

        self.__count += 1

        if self.__count == 20:
            print("render map")
            (minx,maxx) = self.__game.getMap().getLimitsX()
            (miny,maxy) = self.__game.getMap().getLimitsY()

            width  = maxx-minx
            height = maxy-miny

            w = self.__canvas.frameGeometry().width()
            h = self.__canvas.frameGeometry().height()

            dx = 0
            dy = 0

            if width < height:
                dx = math.floor(height*(w/h)-width)
            else:
                dy = math.floor(width*(h/w)-height)
        
            minx -= dx/2
            maxx += dx/2
            miny -= dy/2
            maxy += dy/2
            self.__potential.compute(self.__game.getMap().getList(), minx, maxx, miny, maxy)
            self.__potential.actualisePlot(self.__figure)
            self.__canvas.draw()

            self.__count = 0

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
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        (minx,maxx) = self.__map.getLimitsX()
        (miny,maxy) = self.__map.getLimitsY()

        width  = maxx-minx
        height = maxy-miny

        dx = 0
        dy = 0


        glClearColor(0, 0, 0, 0);

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


    
        #glColor3f( 1.0, 1.5, 0.0 );
        #glPolygonMode(GL_FRONT, GL_FILL);

        glClearColor(0.0,0.0,0.0,0.0)

        glBindTexture(GL_TEXTURE_2D, self.__stars)
        glEnable(GL_TEXTURE_2D)
        glRect(minx, miny, maxx-minx, maxy-miny, z=-1)
        glDisable(GL_TEXTURE_2D)

        # draw the planets
        for planet in self.__map.getList().values():
            x = planet.getX()
            y = planet.getY()
            r = planet.getRadius()
            t = planet.angle

            glBindTexture(GL_TEXTURE_2D, planet.tex)
            glEnable(GL_TEXTURE_2D)
            glRect(x, y, r, r, t)
            glDisable(GL_TEXTURE_2D)

        # TODO: draw the rocket
        if self.__map.getRocket() is not None:
            x = self.__map.getRocket().getX()
            y = self.__map.getRocket().getY()
            r = self.__map.getRocket().getRadius()
            t = self.__map.getRocket().theta

            glBindTexture(GL_TEXTURE_2D, self.__map.getRocket().tex)
            glEnable(GL_TEXTURE_2D)
            glRect(x, y, r, r,t-(22.0/7.0)/4)
            glDisable(GL_TEXTURE_2D)

        glFlush()

    def initializeGL(self):
        glClearColor (0.0, 0.0, 0.0, 0.0);
        glShadeModel(GL_FLAT);
        glEnable(GL_DEPTH_TEST);

        glDisable( GL_LIGHTING)

        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_ALPHA_TEST)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0,1.33,0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        for obj in self.__map.getList().values():
            path = obj.getPath()
            obj.tex = textureFromFile(path)
        path = self.__map.getRocket().getPath()
        self.__map.getRocket().tex = textureFromFile(path)

        self.__stars = textureFromFile('pictures/stars.png')



    def frameReceived(self, frame):
        self.makeCurrent()

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

def glRect(x, y, w, h, rot=0, z=0):
    glLoadIdentity()
    glTranslatef(x, y, 0.0);
    glRotatef(360*rot/(22.0/7.0), 0.0, 0.0, 1.0);

    glMatrixMode(GL_MODELVIEW)

    glBegin(GL_QUADS)
    glTexCoord(0.0, 0.0)
    glVertex3f(-w/1, -h/1,  z)
    glTexCoord(1.0, 0.0)
    glVertex3f( w/1, -h/1,  z)
    glTexCoord(1.0, 1.0)
    glVertex3f( w/1,  h/1,  z)
    glTexCoord(0.0, 1.0)
    glVertex3f(-w/1,  h/1,  z)
    glEnd()

def textureFromFile(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    data = data = numpy.array(list(img.getdata()), numpy.int8)
    width, height = img.size

    glEnable( GL_TEXTURE_2D )
    texture = glGenTextures(1)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glBindTexture(GL_TEXTURE_2D, texture)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
#    texData = [255, 255, 100, 255];
#    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 1, 1, 0, GL_RGBA, GL_UNSIGNED_BYTE, texData)

    return texture

class PlotWidget(FigureCanvasQTAgg):
    def __init__(self, potential, gamemap, parent=None):
        self.__potential = potential
        self.__map = gamemap

        self.__width  = 0
        self.__height = 0

        (xmin, xmax) = self.__map.getLimitsX()
        (ymin, ymax) = self.__map.getLimitsY()


        # initialise the figure
        self.__figure = Figure()
        self.__figure.patch.set_facecolor("None")

        # we want a transparent background
        self.axes = self.__figure.add_subplot(111)
        self.axes.patch.set_alpha(1)

        # initialise this widget
        FigureCanvasQTAgg.__init__(self, self.__figure)
        self.setParent(parent)

        # configure this widget
        FigureCanvasQTAgg.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

        # we need minimal figure
        self.compute_initial_figure()

        # transparent background
        self.setStyleSheet("background-color:transparent;")

    def compute_initial_figure(self):
        (minx,maxx) = self.__map.getLimitsX()
        (miny,maxy) = self.__map.getLimitsY()

        width  = maxx-minx
        height = maxy-miny

        w = self.frameGeometry().width()
        h = self.frameGeometry().height()

        dx = 0
        dy = 0

        if width < height:
            dx = math.floor(height*(w/h)-width)
        else:
            dy = math.floor(width*(h/w)-height)
    
        minx -= dx/2
        maxx += dx/2
        miny -= dy/2
        maxy += dy/2
        
        self.__potential.compute(self.__map.getList(), minx, maxx, miny, maxy)
        self.__potential.initialisePlot(self.__figure)

    def update(self):
        (minx,maxx) = self.__map.getLimitsX()
        (miny,maxy) = self.__map.getLimitsY()

        width  = maxx-minx
        height = maxy-miny

        w = self.frameGeometry().width()
        h = self.frameGeometry().height()

        dx = 0
        dy = 0

        if width < height:
            dx = math.floor(height*(w/h)-width)
        else:
            dy = math.floor(width*(h/w)-height)
    
        minx -= dx/2
        maxx += dx/2
        miny -= dy/2
        maxy += dy/2
        self.__potential.compute(self.__map.getList(), minx, maxx, miny, maxy)
        self.__potential.actualisePlot()
        #self.__figure.canvas.draw()
        self.draw()

