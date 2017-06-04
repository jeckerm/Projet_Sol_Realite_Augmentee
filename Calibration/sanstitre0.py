#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:27:53 2017

@author: ftorre
"""

from PyQt4 import QtGui, QtCore
im = QtGui.QImage("./damier.png")
improcessed = QtGui.QImage(1920, 1080, im.format())
improcessed.fill(QtCore.Qt.white)

xA = 0
yA = 0

xB = 1920 * 458
yB = 1920 * 2.35

xC = 1080 * (-2.64)
yC = 1080 * 461

xD = 1920 * 458 + 1080 * (-2.64)
yD = 1920 * 2.35 + 1080 * 461

q1 = 1920/max(abs(xA-xB), abs(xC-xD))
print(q1)
q2 = 1080/max(abs(yA-yC), abs(yB-yD))
print(q2)

xcor = min (xA, xB, xC, yC)
ycor = min(yA, yB, yC, yD)


q = min(q1,q2)

for i in range(1921):
    for j in range(1081):
        L= [0,0,0,0]
        x = int(q*(i * 458 + j * (-2.64) - xcor))
        #print (x)
        if x>1920:
            #print('xerror+')
            L[0] = 1
        if x<0:
            #print('xerror-')
            L[1] = 1
        y = int(q*(i * 2.35 + j * 461 - ycor))
        #print (y)
        if y>1080 :
            #print('yerror+')
            #print(y)
            L[2] = 1
        if y<0:
            #print('yerror-')
            L[3] = 1
        if x>=0 and x<=1920 and y>=0 and y<=1080:
            improcessed.setPixel(x, y, im.pixel(i,j))
print(L)
        
        
print("finish")
improcessed.save("./damiertransform.png")
