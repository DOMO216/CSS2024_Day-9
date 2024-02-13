#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:42:15 2024

@author: thabangmolefi
"""
# Euler Method
h=0.1 #stepsize
x0 = 0 # initial x-value
xmax = 0.5  # final x-value
y0 = 1 # initial y-value


y_euler = [y0]
f = lambda x,y: 2*y**(3/2)

while x0<xmax:
    y1 = y0 + f(x0,y0)*h 
    y_euler.append(y1)
    y0=y1
    x0 = round(x0+h,10)
    
    

    
    