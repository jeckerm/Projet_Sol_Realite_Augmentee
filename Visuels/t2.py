# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:18:41 2017

@author: henry
"""

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