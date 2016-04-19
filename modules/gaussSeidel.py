#!/usr/bin/env python

##########################################################################################################
# Calculo Numerico - 2016 de la Universidad del Comahue. Centro Regional Bariloche
# Profesorado y Licenciatura en Matematicas
# http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 
# Codigo del libro:
# Numerical Methods in Engineering with Python 3 3rd Edition (2013)
# by Jaan Kiusalaas
# Publisher: Cambridge University Press
# ISBN-10: 1107033853
# ISBN-13: 978-1107033856
# Para incluir la implementacion en el notebook agregar
# import sys
# sys.path.append("path relativo a /modules/")

# Implementacion gaussSeidel
# x,numIter,omega = gaussSeidel(iterEqs,x,tol = 1.0e-9)
# Gauss-Seidel method for solving [A]{x} = {b}.
# The matrix [A] should be sparse. User must supply the
# function iterEqs(x,omega) that returns the improved {x},
# given the current {x} ('omega' is the relaxation factor).
##########################################################################################################

from numpy import dot
from math import sqrt

def gaussSeidel(iterEqs,x,tol = 1.0e-9):
    
    omega = 1.0
    k = 10
    p = 1
    for i in range(1,501):
        xOld = x.copy()
        x = iterEqs(x,omega)
        dx = sqrt(dot(x-xOld,x-xOld))
        if dx < tol: return x,i,omega
      # Compute relaxation factor after k+p iterations
        if i == k: dx1 = dx
        if i == k + p:
            dx2 = dx
            omega = 2.0/(1.0 + sqrt(1.0 - (dx2/dx1)**(1.0/p)))
    print 'Gauss-Seidel failed to converge'    
