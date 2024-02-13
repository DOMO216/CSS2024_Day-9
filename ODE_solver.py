#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:27:04 2024

@author: thabangmolefi
"""

import numpy as np
from scipy.integrate import solve_ivp

# Right -hand side of ODE
f = lambda t,y: np.sin(t)**2 * y
 
# t-values for which ODE is solved
t_eval = np.linspace(0, 10)

sol = solve_ivp(f, [t_eval[0],t_eval[-1]],y0=[1], method='RK45', t_eval=t_eval)
                
sol.t # Returns t-values shape=(len(t_eval),)
sol.y # Returns y-values t_eval)) shape=(len(y0),len(


sol.y.reshape(sol.t.shape) # shape=(len(t_eval),)