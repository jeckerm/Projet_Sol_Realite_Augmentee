# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:25:09 2017

@author: henry
"""

import sys
import numpy as np
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtCore import QObject


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
        self.c1 = QtGui.QLineEdit("0",self)
        self.c2 = QtGui.QLineEdit("0",self)
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

    def sendDataCross(self):
        try:
            self.mainWindow.widget.damier.transformers(float(self.c1.text()), float(self.c2.text()))
            self.close()
        except:
            print("Must be float values or Non-zero")

class ImageDamier():
    
    def __init__(self):
        
        self.image = QtGui.QImage(1920, 1080, QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        self.p = QtGui.QPainter(self.image) 
        self.p.setBrush(QtGui.QBrush(QtCore.Qt.black))
        #for i in range(4):
        #    for j in range(4):
        #        if (i + j) % 2 == 0:
        #            self.p.drawRect(i * 420, j * 270, 420, 270)
                
    def transformers(self, c11, c21, c12, c22):
        
        xA = 0
        yA = 0
        
        xB = self.image.width() * c11
        yB = self.image.width() * c21
        
        xC = self.image.height() * c12
        yC = self.image.height() * c22
        
        xD = self.image.width() * c11 + self.image.height() * c21
        yD = self.image.width() * c12 + self.image.height() * c22
        
        qx = 1920/max(abs(xA-xB), abs(xC-xD))
        qy = 1080/max(abs(yA-yC), abs(yB-yD))
        
        improcessed = QtGui.QImage(1920,1080,QtGui.QImage.Format_RGB32)
        improcessed.fill(QtCore.Qt.white)
        for i in range(1920):
            for j in range(1080):
              
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
        self.p = self.damier.p
        self.image = self.damier.image

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
        self.p = self.widget.p
        self.image = self.widget.image
        self.widget.punched.connect(self.say_punched)
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
            self.widget.traceCercle(100,100,0,0)
            self.image.save("./newdamier.png", format = "PNG" )
        elif event.key() == QtCore.Qt.Key_B:
            self.widget.punch()
        else:
            event.ignore()
    


    #@pyqtSlot()
    def say_punched(self):
        #L est la liste des coordonnées des croix que l'on veut afficher
        #Chaque élément k de la liste L est sous la forme :
        #k[0], k[1] : coordonnées du centre de la croix
        I = QtGui.QImage(1920, 1080, QtGui.QImage.Format_RGB32)
        I.fill(QtCore.Qt.white)
        L = [[1257,489],[775,950],[781,539],[1075,672]]
        #-86 379    1046  4565
        self.p.setBrush(QtCore.Qt.black)
        #self.p.setStyleSheet("border: 0px")

        for k in L:
            self.p.drawRect(k[0]-3, k[1]-20, 6, 40)
            self.p.drawRect(k[0]-20, k[1]-3, 40, 6)
        print('Bag was punched.')
    
app = QtGui.QApplication(sys.argv)

ex = Window()
sys.exit(app.exec_())
