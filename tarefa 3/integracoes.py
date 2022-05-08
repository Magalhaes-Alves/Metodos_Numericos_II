from math import sin, fabs, inf, cos,acos


def f(x):
    
    return (sin(2*x) + 4*(x**2) + 3*x)**2


def integracoesFechadas(xi, xf, grau):
    h = (xf  - xi)/(grau)

    if grau==1:
        return (h*(f(xi)+f(xf)))/2
    elif grau==2:
        return ((h/3) * (f(xi) + 4*f(xi+h)+f(xf)))
    elif grau==3:
        return ((3*h/8) * (f(xi) + 3*f(xi+h) + 3*f(xi+2*h) + f(xf)))
    else:
        return ((2*h/45) * (7*f(xi) + 32*f(xi+h) + 12*f(xi+2*h) + 32*f(xi+3*h) + 7*f(xf)))


def integracoesAbertas(xi, xf, grau):
    h = (xf  - xi)/(grau + 2)

    if grau==1:
        return ((3*h/2) * (f(xi+h)+f(xi+2*h)))
    elif grau==2:
        return ((4*h/3) * (2*f(xi+h) - f(xi+2*h) + 2*f(xi+3*h)))
    elif grau==3:
        return ((5*h/24) * (11*f(xi+h)+f(xi+2*h)+f(xi+3*h)+11*f(xi+4*h)))
    else:
        return ((6*h/20) * (11*f(xi+h)-14*f(xi+2*h)+26*f(xi+3*h)-14*f(xi+4*h)+11*f(xi+5*h)))


def integracao(a,b,e,grau, aberta = False):
    n=1
    
    if(aberta==False):
        integral_nova = integracoesFechadas(a,b,grau)
    else:
        integral_nova = integracoesAbertas(a,b,grau)
    
    erro=inf
    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        delta = (b-a)/n
        integral_nova=0
        for j in range(n):
            xi = a +j*delta
            xf = xi +delta
            if(aberta==False):
                integral_nova = integral_nova + integracoesFechadas(xi,xf,grau)
            else:
                integral_nova = integral_nova + integracoesAbertas(xi,xf,grau)
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    print(f'Partições:{n}')
    print(f'Integral encontrada: {integral_nova}')