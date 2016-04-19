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

# Implementacion conjGrad
# x, numIter = conjGrad(Av,x,b,tol=1.0e-9)
# Conjugate gradient method for solving [A]{x} = {b}.
# The matrix [A] should be sparse. User must supply
# the function Av(v) that returns the vector [A]{v}.
##########################################################################################################

from numpy import dot
from math import sqrt

def conjGrad(Av,x,b,tol=1.0e-9):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in range(n):
        u = Av(s)
        alpha = dot(s,r)/dot(s,u)
        x = x + alpha*s
        r = b - Av(x)
        if(sqrt(dot(r,r))) < tol:
            break
        else:
            beta = -dot(r,u)/dot(s,u)
            s = r + beta*s
    return x,i


    
