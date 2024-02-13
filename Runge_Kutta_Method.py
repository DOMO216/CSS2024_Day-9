#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:53:03 2024

@author: thabangmolefi
"""

# Runge-kutta Method
h=0.1 # stepsize
x0 = 0 # initial x-value
xmax = 0.5 # final x-value
y0 = 1 # initial y-value

y_rk2 = [y0]

f = lambda x,y: 2*y**(3/2) 

while x0<xmax:
    a1 = f(x0,y0)*h
    a2 = f(x0 + h, y0 + a1)*h
    y1 = y0 + 0.5 * (a1 + a2)
    y_rk2.append(y1)
    y0=y1
    x0 = round(x0+h,10)