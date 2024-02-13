#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:01:00 2024

@author: thabangmolefi
"""

import numpy as np 

h=0.5
x0 = 0
xmax = 5
y0 = 0

y_rk4 = [y0] 
f = lambda x,y: np.sin(x)**2 * y
while x0<xmax:
    b1 = f(x0,y0)*h
    b2 = f(x0 + 0.5*h, y0 + 0.5*b1)*h
    b3 = f(x0 + 0.5*h, y0 + 0.5*b2)*h
    b4 = f(x0 + h, y0 + b3)*h
    y1 = y0 + 1/6 * (b1 + 2*b2 + 2*b3 + b4)
    y_rk4.append(y1)
    y0=y1
    x0 = round(x0+h,10)