# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:25:09 2017

@author: henry
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, pyqtSlot


class Popup(QtGui.QWidget):
    def __init__(self, parent):
        super(Popup, self).__init__()
        self.setFixedSize(200,200)
        self.mainWindow = parent
        self.layout = QtGui.QGridLayout(self)
        self.c11 = QtGui.QLineEdit("0", self)
        self.c21 = QtGui.QLineEdit("0", self)
        self.c12 = QtGui.QLineEdit("0", self)
        self.c22 = QtGui.QLineEdit("0", self)
        self.enter = QtGui.QPushButton("Process", self)
        self.enter.clicked.connect(self.sendData)
        self.layout.addWidget(self.c11, 0, 0)
        self.layout.addWidget(self.c21, 1, 0)
        self.layout.addWidget(self.c12, 0, 1)
        self.layout.addWidget(self.c22, 1, 1)
        self.layout.addWidget(self.enter, 2, 1)
        self.setLayout(self.layout)
        
    def sendData(self):
        try:
            self.mainWindow.widget.damier.transformers(float(self.c11.text()), float(self.c21.text()), float(self.c12.text()), float(self.c22.text()))
            self.close()
        except:
            print("Must be float values or Non-zero")

class ImageDamier():
    
    def __init__(self):
        
        self.image = QtGui.QImage(384, 216, QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        p = QtGui.QPainter(self.image) 
        p.setBrush(QtGui.QBrush(QtCore.Qt.black))
        for i in range(4):
            for j in range(4):
                if (i + j) % 2 == 0:
                    p.drawRect(i * 96, j * 54, 96, 54)
                
    def transformers(self, c11, c21, c12, c22):
        
        xA = 0
        yA = 0
        
        xB = self.image.width() * c11
        yB = self.image.width() * c21
        
        xC = self.image.height() * c12
        yC = self.image.height() * c22
        
        xD = self.image.width() * c11 + self.image.height() * c21
        yD = self.image.width() * c12 + self.image.height() * c22
        
        qx = 384/max(abs(xA-xB), abs(xC-xD))
        qy = 216/max(abs(yA-yC), abs(yB-yD))
        
        improcessed = QtGui.QImage(384,216,QtGui.QImage.Format_RGB32)
        improcessed.fill(QtCore.Qt.white)
        for i in range(385):
            for j in range(216):
                
                x = (i * c11 + j * c21) * qx 
                y = (i * c12 + j * c22) * qy
                
                improcessed.setPixel(x, y, self.image.pixel(i,j))
        
        self.image = improcessed
    

        
class Damier(QtGui.QWidget):
    
    punched = pyqtSignal()
    
    def __init__(self):
        
        super(Damier, self).__init__()
        self.damier = ImageDamier()
        self.circles = []

    def paintEvent(self, event):
        p = QtGui.QPainter(self) 
        p.drawImage(0, 0, self.damier.image.scaled(1920,1080))
        for circle in self.circles:
            p.setBrush(QtCore.Qt.red)
            p.drawEllipse(circle[0], circle[1], circle[2], circle[3])
        self.circles = []
        
    def transformDamier(self, c11, c21, c12, c22):
        self.damier.transformers(c11, c21, c12, c22) #(458, -2.64, 2.35, 461)
        self.update()
    
    def traceCercle(self, x, y, width, height):
        
        self.circles.append([x,y,width,height])
        self.repaint()
    
    def punch(self):
        self.punched.emit()
        
class Window(QtGui.QMainWindow):
    
    

    def __init__(self):
        
        super(Window, self).__init__()
        
        self.widget = Damier()
        self.widget.punched.connect(say_punched)
        self.popup = Popup(self)
        
        self.setCentralWidget(self.widget)
        self.setGeometry(0, 0, 1920, 1080)
        self.show()
        
    def keyPressEvent(self, event):
        
        if event.key() == QtCore.Qt.Key_Space:
            if not self.popup.isVisible():
                self.popup.show()
            else :
                print("popup already opened")
            event.accept()
        elif event.key() == QtCore.Qt.Key_A:
            self.widget.traceCercle(100,100,200,200)
        elif event.key() == QtCore.Qt.Key_B:
            self.widget.punch()
        else:
            event.ignore()
    

    
        
@pyqtSlot()
def say_punched():
    print('Bag was punched.')
    
app = QtGui.QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())