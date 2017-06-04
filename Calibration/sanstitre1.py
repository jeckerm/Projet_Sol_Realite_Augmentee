#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:11:41 2017

@author: ftorre
"""

import sys
from PyQt4 import QtGui, QtCore


class Damier(QtGui.QWidget):
    
    def __init__(self):
        
        super(Damier, self).__init__()
        
        self.image = QtGui.QPixmap(1920, 1080)
        self.image.fill(QtCore.Qt.white)
        
        self.des = False
        
    def paintEvent(self, event):
        p = QtGui.QPainter(self) 
        p.drawPixmap(0,0,self.image)
        
    def mousePressEvent(self, event):
        if not self.des:
            
            p = QtGui.QPainter(self.image) 
            
            p.setBrush(QtGui.QBrush(QtCore.Qt.black))
            
            for i in range(4):
                for j in range(4):
                    
                    if (i + j) % 2 == 0:
                        p.drawRect(i * 480, j * 270, 480, 270 )
                        print ("drawn")
        
            #self.image = self.render(p)
            self.des = True
            self.image.save("./damier.png", format = "PNG" )
        else:
            self.image = self.image.transformed(QtGui.QTransform(0,1,0,1,-4,1,0,1,0))
        self.repaint()
        print('hello')
        
            
class Window(QtGui.QMainWindow):

    def __init__(self):
        
        super(Window, self).__init__()
        
        self.image = Damier()
        
        self.setCentralWidget(self.image)
        self.setGeometry(0, 0, 1920, 1080)
        self.show()
    
app = QtGui.QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())