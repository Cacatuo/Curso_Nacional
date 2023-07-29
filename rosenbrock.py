# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:54:47 2023
Rosenbrock function
@author: Camilo Acosta
"""

import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var(initialize=1.5)
model.y = pyo.Var(initialize=1.5)

def rosenbrock(m):
    return (1.0-m.x)**2+100.0*(m.y-m.x**2)**2
model.obj = pyo.Objective(rule=rosenbrock, sense = pyo.minimize)

pyo.SolverFactory('ipopt').solve(model,tee=True)
model.pprint()

# graficar la función de rosenbrock
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

b = 100 # valor del multiplicador de rosenbrock
f = lambda x,y: (x-1)**2 + b*(y-x**2)**2
figRos = plt.figure(figsize=(12, 7))
axRos = figRos.gca(projection='3d')

# Evaluar la función
X = np.arange(-2,2,0.15)
Y = np.arange(-1,3,0.15)
X,Y = np.meshgrid(X,Y)
Z = f(X,Y)
# crear la superficie
surf = axRos.plot_surface(X,Y,Z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
axRos.set_zlim(0, 1000)
figRos.colorbar(surf, shrink=0.5, aspect=10)
plt.show()