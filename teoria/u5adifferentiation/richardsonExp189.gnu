#run gnuplot
# in gnuplot command line type
# load "./richardsonExp189.gnu"
f(x)=exp(-x)
h1 = 0.64
x0 = 1.
df2(x,h)= (f(x-h)-2*f(x)+f(x+h))/h**2
h2 = h1*0.5
G = (2**2*df2(x0,h2)-df2(x0,h1))/(2**2-1)
pri "=========================================="
pri "Derivada segunda de f(x)=exp(-x) en x = 1"
pri "=========================================="
pri "exp(-1) = ", exp(-1.)
pri "d2f/dx2(h = 0.64)= ", df2(x0,h1)
pri "d2f/dx2(h = 0.32)= ",df2(x0,h2)
pri "Richardson = ",  G
pri "Errores"
pri "======="
pri "Error con h1: ",exp(-1.)- df2(x0,h1)
pri "Error con h2: ", exp(-1.)- df2(x0,h2)
pri "Error con Richardson: ", exp(-1.)- G
