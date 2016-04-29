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

# Implementacion rational
# p = rational(xData,yData,x)
# Evaluates the diagonal rational function interpolant p(x)
# that passes through the data points
##########################################################################################################

import numpy as np
def rational(xData,yData,x):
	m = len(xData)
	r = yData.copy()
	rOld = np.zeros(m)
	for k in range(m-1):
		for i in range(m-k-1):
			if abs(x - xData[i+k+1]) < 1.0e-9:
				return yData[i+k+1]
			else:
				c1 = r[i+1] - r[i]
				c2 = r[i+1] - rOld[i+1]
				c3 = (x - xData[i])/(x - xData[i+k+1])
				r[i] = r[i+1] + c1/(c3*(1.0 - c1/c2) - 1.0)
				rOld[i+1] = r[i+1]
	return r[0]