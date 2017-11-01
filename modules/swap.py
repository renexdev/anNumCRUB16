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

# Implementacion swap
# Swaps rows i and j of vector or matrix [v].
# swapCols(v,i,j). Swaps columns i and j of matrix [v].

##########################################################################################################
   
def swapRows(v,i,j):
	#print v
	#print len(v.shape
	#this len v.shape implementation should be checked!
	if len(v.shape) == 1: v[i],v[j] = v[j],v[i]
	else:
		temp = v[i].copy()
		v[i] = v[j]
		v[j] = temp
   
def swapCols(v,i,j):
    temp = v[:,j].copy()
    v[:,j] = v[:,i]
    v[:,i] = temp
