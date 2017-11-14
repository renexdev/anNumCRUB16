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

# Implementacion newtonRaphson
# root = newtonRaphson(f,df,a,b,tol=1.0e-9).
# Finds a root of f(x) = 0 by combining the Newton-Raphson
# method with bisection. The root must be bracketed in (a,b).
# Calls user-supplied functions f(x) and its derivative df(x). 
##########################################################################################################

def newtonRaphson(f,df,a,b,tol=1.0e-9):
    import error
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0: error.err('Root is not bracketed')
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
        if abs(fx) < tol: return x
      # Tighten the brackets on the root 
        if fa*fx < 0.0:
            b = x  
        else:                  
            a = x; fa = fx
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b-a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print 'Too many iterations in Newton-Raphson'