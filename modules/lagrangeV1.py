#!/usr/bin/env python

##########################################################################################################
# Calculo Numerico - 2016 de la Universidad del Comahue. Centro Regional Bariloche
# Profesorado y Licenciatura en Matematicas
# http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 
# ISBN-13: 978-1107033856
# Para incluir la implementacion en el notebook agregar
# import sys
# sys.path.append("path relativo a /modules/")

# Implementacion Lagrange

##########################################################################################################

def lagrange(points):
  def P(x):
    total = 0
    n = len(points)
    for i in xrange(n):
      xi, yi = points[i]
      
      def g(i, n):
        
        tot_mul = 1
        for j in xrange(n):
          if i == j:
            continue
          xj, yj = points[j]
          tot_mul *= (x - xj) / float(xi - xj)
          
        return tot_mul 

      total += yi * g(i, n)
    return total
  return P 