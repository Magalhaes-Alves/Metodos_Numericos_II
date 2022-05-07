from math import fabs, inf
from math import cos

def f(x):
    
    return cos(x)
    

def simpson(xi, xf):
    
    h = (xf - xi)/2
    
    return ((h/3) * (f(xi) + 4*f(xi+h)+f(xf)))


def integracao(a,b,e):
    n=1
    integral_nova = simpson(a,b)
    erro=inf
    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        delta = (b-a)/n
        integral_nova=0
        for j in range(n):
            xi = a +j*delta
            xf = xi +delta
            integral_nova =integral_nova +simpson(xi,xf)
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    print(f'Partições:{n}')
    print(f'Integral encontrada: {integral_nova}')