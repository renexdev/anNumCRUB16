#!/usr/bin/env python

##########################################################################################################
# Calculo Numerico - 2016 de la Universidad del Comahue. Centro Regional Bariloche
# Profesorado y Licenciatura en Matematicas
# http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

# Para incluir la implementacion en el notebook agregar
# import sys
# sys.path.append("path relativo a /modules/")

# Implementacion ridder
# root = ridder(f,a,b,tol=1.0e-9).
# Finds a root of f(x) = 0 with Ridders method.
# The root must be bracketed in (a,b).
##########################################################################################################
import error
import math
from numpy import sign

def ridder(f,a,b,tol=1.0e-9):
	fa = f(a)
	if fa == 0.0: return a
	fb = f(b)
	if fb == 0.0: return b
	#if sign(f2)!= sign(f3): x1 = x3; f1 = f3
	for i in range(30):
		# Compute the improved root x from Ridders formula
		c = 0.5*(a + b); fc = f(c)
		s = math.sqrt(fc**2 - fa*fb)
		if s == 0.0: return None
		dx = (c - a)*fc/s
		if (fa - fb) < 0.0: dx = -dx
		x = c + dx; fx = f(x)
		# Test for convergence
		if i > 0:
			if abs(x - xOld) < tol*max(abs(x),1.0): return x
		xOld = x
		# Re-bracket the root as tightly as possible
		if sign(fc) == sign(fx):
			if sign(fa)!= sign(fx): b = x; fb = fx
			else: a = x; fa = fx
		else:
			a = c; b = x; fa = fc; fb = fx
	return None
	print("Too many iterations")