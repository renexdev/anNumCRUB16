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

# Implementacion romberg
# I,nPanels = romberg(f,a,b,tol=1.0e-6).
# Romberg intergration of f(x) from x = a to b.
# Returns the integral and the number of panels used.
##########################################################################################################
from numpy import zeros
from trapezoid import *

def romberg(f,a,b,tol=1.0e-6):
    
    def richardson(r,k):
        for j in range(k-1,0,-1):
            const = 4.0**(k-j)
            r[j] = (const*r[j+1] - r[j])/(const - 1.0)
        return r
     
    r = zeros((21),type=float)
    r[1] = trapezoid(f,a,b,0.0,1)
    r_old = r[1]
    for k in range(2,21):
        r[k] = trapezoid(f,a,b,r[k-1],k)
        r = richardson(r,k)
        if abs(r[1]-r_old) < tol*max(abs(r[1]),1.0):
            return r[1],2**(k-1)
        r_old = r[1]
    print "Romberg quadrature did not converge"



