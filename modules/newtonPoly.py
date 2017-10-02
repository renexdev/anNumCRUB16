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

# Implementacion newtonPoly
# p = evalPoly(a,xData,x).
# Evaluates Newton's polynomial p at x. The coefficient
#vector 'a' can be computed by the function 'coeffts'.
# a = coeffts(xData,yData).
# Computes the coefficients of Newton's polynomial.
##########################################################################################################

def evalPoly(a,xData,x):
    n = len(xData) - 1  # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

def coeffts(xData,yData):
    m = len(xData)  # Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a
