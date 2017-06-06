# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:17:22 2017

@author: henry
"""

def transformers(self,):
        
        improcessed = QtGui.QImage(1920,1080,QtGui.QImage.Format_RGB32)
        improcessed.fill(QtCore.Qt.white)
        for i in range(1921):
            for j in range(1081):
                
                x = i * 0.30 + j * (-0.02)
                y = i * 0.046 + j * 0.36
                
                improcessed.setPixel(int(x), int(y), self.image.pixel(i,j))
        
        self.image = improcessed