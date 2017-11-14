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

# Utilidades 
##########################################################################################################

import numpy as np

def LEPrint(A,b):
	#Imprime un sistema de ecuaciones Ax=b
	print "Linear system:"
	for i in range(A.shape[0]):
	    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
	    print " + ".join(row) + "=" + "%.2f"%b[i] + "\t (%d)"%(i+1)
	return;
