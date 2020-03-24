#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:47:16 2020

@author: Kabbani
"""

import numpy as np
import cv2

cap=cv2.VideoCapture('video_teste.mp4')


while(cap.isOpened()):
    
    ret,frame=cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,50,150,apertureSize = 3) 

    lines = cv2.HoughLines(edges,1,np.pi/180, 200) 

    linha_achada1=False  
    linha_achada=False       
    h1=0
    m1=0
    m2=0
    h2=0
    for linha in lines: #usamos como referencia: https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
        for r,theta in linha: 
            a = np.cos(theta) 
            b = np.sin(theta)  
            x0 = a*r 
            y0 = b*r 
            x1 = int(x0 + 1000*(-b))  
            y1 = int(y0 + 1000*(a))  
            x2 = int(x0 - 1000*(-b))  
            y2 = int(y0 - 1000*(a)) 
            if (x2-x1)!=0:
                coef1=(y2-y1)/(x2-x1)
            if coef1 < -0.25 and coef1 > -3:
                if linha_achada1==False:
                    linha_achada1=True
                    m1=coef1
                    h1=(y1-coef1*x1)
                    cv2.line(frame,(x1,y1), (x2,y2), (0,0,255),2)
            elif coef1 > 0.25 and coef1<3:
                if linha_achada==False:
                    linha_achada=True
                    m2=coef1
                    h2=(y1-coef1*x1)
                    cv2.line(frame,(x1,y1), (x2,y2), (0,0,255),2)
    if (m1-m2)!=0:                    
        xinter=int((h2-h1)/(m1-m2))
    yinter=int(m1*xinter + h1) 
    cv2.circle(frame,(xinter,yinter), 10, (0,255,0), -1)

    cv2.imshow('linhas',frame)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()