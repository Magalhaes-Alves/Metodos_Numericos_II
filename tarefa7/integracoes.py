from math import tanh, sinh, cosh, pi, inf, fabs

def f(x, tipo):
    if tipo == 1:
        return 1 / pow(pow(x, 2.0), (1 / 3.0))
    else:
        return 1 / pow(4 - (x * x), 1/2.0)


def x(s, a, b, tipo):
    if tipo == 1:
        return ((a + b) / 2.0 + (b - a) * tanh(s) / 2.0)
    else:
        return (((a + b) / 2.0) + (((b - a) / 2.0) * tanh((pi / 2.0) * sinh(s))))


def dx(s, a, b, tipo):
    if tipo == 1:
        return (b - a) / (2 * (pow(cosh(s), 2)))
    else:
        return ((b - a) / 2.0) * ((pi / 2.0) * (cosh(s) / (pow(cosh((pi / 2.0) * sinh(s)), 2.0))))


def fb(s, a, b, tipofunc, tipoexp):
    return f(x(s, a, b, tipoexp), tipofunc) * dx(s, a, b, tipoexp)


def integracoesFechadas(xi, xf, grau, a, b, tipofunc, tipoexp):
    h = (xf  - xi)/(grau)

    if grau==1:
        return (h*(fb(xi, a, b, tipofunc, tipoexp)+fb(xf, a, b, tipofunc, tipoexp)))/2
    elif grau==2:
        return ((h/3) * (fb(xi, a, b, tipofunc, tipoexp) + 4*fb(xi+h, a, b, tipofunc, tipoexp)+fb(xf, a, b, tipofunc, tipoexp)))
    elif grau==3:
        return ((3*h/8) * (fb(xi, a, b, tipofunc, tipoexp) + 3*fb(xi+h, a, b, tipofunc, tipoexp) + 3*fb(xi+2*h, a, b, tipofunc, tipoexp) + fb(xf, a, b, tipofunc, tipoexp)))
    else:
        return ((2*h/45) * (7*fb(xi, a, b, tipofunc, tipoexp) + 32*fb(xi+h, a, b, tipofunc, tipoexp) + 12*fb(xi+2*h, a, b, tipofunc, tipoexp) + 32*fb(xi+3*h, a, b, tipofunc, tipoexp) + 7*fb(xf, a, b, tipofunc, tipoexp)))


def integracoesAbertas(xi, xf, grau,a ,b, tipofunc, tipoexp):
    h = (xf  - xi)/(grau + 2)

    if grau==1:
        return ((3*h/2) * (fb(xi+h, a, b, tipofunc, tipoexp)+fb(xi+2*h, a, b, tipofunc, tipoexp)))
    elif grau==2:
        return ((4*h/3) * (2*fb(xi+h, a, b, tipofunc, tipoexp) - fb(xi+2*h, a, b, tipofunc, tipoexp) + 2*fb(xi+3*h, a, b, tipofunc, tipoexp)))
    elif grau==3:
        return ((5*h/24) * (11*fb(xi+h, a, b, tipofunc, tipoexp)+fb(xi+2*h, a, b, tipofunc, tipoexp)+fb(xi+3*h, a, b, tipofunc, tipoexp)+11*fb(xi+4*h, a, b, tipofunc, tipoexp)))
    else:
        return ((6*h/20) * (11*fb(xi+h, a, b, tipofunc, tipoexp)-14*fb(xi+2*h, a, b, tipofunc, tipoexp)+26*fb(xi+3*h, a, b, tipofunc, tipoexp)-14*fb(xi+4*h, a, b, tipofunc, tipoexp)+11*fb(xi+5*h, a, b, tipofunc, tipoexp)))


def calcularNewtonCotes(x0i,x0f, a, b, e,grau, tipofunc, tipoexp, aberta):
    n=1
    
    if(aberta==False):
        integral_nova = integracoesFechadas(x0i, x0f, grau, a, b, tipofunc, tipoexp)
    else:
        integral_nova = integracoesAbertas(x0i, x0f, grau, a, b, tipofunc, tipoexp)
    print(integral_nova)
    erro=inf
    
    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        
        delta = (x0f-x0i)/n
        integral_nova=0
        for j in range(n):
            xi = x0i +j*delta
            xf = xi +delta
            if(aberta==False):
                integral_nova = integral_nova + integracoesFechadas(xi, xf, grau, a, b, tipofunc, tipoexp)
            else:
                integral_nova = integral_nova + integracoesAbertas(xi, xf, grau,a , b, tipofunc, tipoexp)
       
        erro =fabs((integral_nova-integral_velha)/integral_nova)

    return integral_nova


def gaussLegrende2Pontos(a,b,limiteInferior,limiteSuperior,e,tipofunc,tipoexp):

    iteracoes = 1
    n = 1

    xa1 = ((a + b) / 2) + ((b-a)/2)*(-0.577350269)
    xa2 = ((a + b) / 2) + ((b-a)/2)*(0.577350269)

    #w1=w2=1
    #Ro é a fórmula do somatório de f(x(alphak))wk
    integral_velha = ((b-a)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp)*1 + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp)*1 )
    integral_nova = integral_velha
    erro=inf

    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        iteracoes += 1
        delta = (b-a)/n

        sum=0
        x0 = a
        while(x0<b):
            #X0 + XF = X0 + Xo + Variacao
			#XF - X0 = X0 + Variacao - X0 = Variacao
            xa1 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(-0.577350269)

            xa2 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(0.577350269)

            sum += ((delta)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp) + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    return integral_nova


def gaussLegrende3Pontos(a,b,limiteInferior,limiteSuperior,e,tipofunc,tipoexp):

    iteracoes = 1
    n = 1
    xa1 = ((a + b) / 2) + ((b-a)/2)*(-0.774596669)
    #alpha1 = -raiz(3/5)
    xa2 = ((a + b) / 2)
    #alpha2 = 0
    xa3 = ((a + b) / 2) + ((b-a)/2)*(0.774596669)
    #alpha3 = raiz(3/5)

    #Ro é a fórmula do somatório de f(x(alphak))wk
    integral_velha = ((b-a)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(5.0/9.0) + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(8.0/9.0) + fb(xa3,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(5.0/9.0) )
    integral_nova = integral_velha
    erro=inf

    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        iteracoes += 1
        delta = (b-a)/n

        sum=0
        x0 = a
        while(x0<b):
            #X0 + XF = X0 + Xo + Variacao
			#XF - X0 = X0 + Variacao - X0 = Variacao

            xa1 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(-0.774596669)

            xa2 = ((x0 + x0 + delta) / 2)

            xa3 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(0.774596669)

            sum += ((delta)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(5.0/9.0) + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(8.0/9.0) + fb(xa3,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(5.0/9.0) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
        print(integral_nova)
    return integral_nova


def gaussLegrende4Pontos(a,b,limiteInferior,limiteSuperior,e,tipofunc,tipoexp):
    iteracoes = 1
    n = 1
    xa1 = ((a + b) / 2) + ((b-a)/2)*(-0.861136311)
    #alpha1 = -0.861136311
    xa2 =  ((a + b) / 2) + ((b-a)/2)*(-0.339981043)
    #alpha2 = -0.339981043
    xa3 = ((a + b) / 2) + ((b-a)/2)*(0.339981043)
    #alpha3 = 0.339981043
    xa4 = ((a + b) / 2) + ((b-a)/2)*(0.861136311)
    #alpha4 = 0.861136311

    #Ro é a fórmula do somatório de f(x(alphak))wk
    integral_velha = ((b-a)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.3478548451) + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.6521451548) + fb(xa3,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.6521451548) + fb(xa4,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.3478548451) )
    integral_nova = integral_velha
    erro=inf

    while (erro> e):
        integral_velha = integral_nova
        n=n*2
        iteracoes += 1
        delta = (b-a)/n

        sum=0
        x0 = a
        while(x0<b):
            #X0 + XF = X0 + Xo + Variacao
			#XF - X0 = X0 + Variacao - X0 = Variacao

            xa1 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(-0.861136311)

            xa2 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(-0.339981043)

            xa3 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(0.339981043)

            xa4 = ((x0 + x0 + delta) / 2) + ((delta)/2)*(0.861136311)

            sum += ((delta)/2)*( fb(xa1,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.3478548451) + fb(xa2,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.6521451548) + fb(xa3,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.6521451548) + fb(xa4,limiteInferior,limiteSuperior,tipofunc,tipoexp)*(0.3478548451) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    return integral_nova


def integrarNewtonCotes(a, b, e,grau, tipofunc, tipoexp, aberta = False):

    if tipofunc == 1:
        c = 0.5
    else:
        c = 0.5
    r1 = calcularNewtonCotes(-c,c, a, b, e,grau, tipofunc, tipoexp, aberta)
    print(r1)
    erro = inf
    i = 0

    while(erro>e):
        r0 = r1
        if tipofunc == 1:
            c += 0.01
        else:
            c += 0.3
        i+=1
        print(r1)
        r1 = calcularNewtonCotes(-c,c, a, b, e,grau, tipofunc, tipoexp, aberta)
        print(r1)
        erro = fabs(r0-r1)
    print(f"Integral:{r1}")


def integrarGaussLegrende(a, b, e,grau, tipofunc, tipoexp):
    if tipofunc == 1:
        c = 0.50
    else:
        c = 0.5
   
    if grau == 2:
        r1 = gaussLegrende2Pontos(-c,c, a, b, e,tipofunc, tipoexp)
    elif grau==3:
        r1 = gaussLegrende3Pontos(-c,c, a, b, e,tipofunc, tipoexp)
    else:
        r1 = gaussLegrende4Pontos(-c,c, a, b, e,tipofunc, tipoexp)

    erro = inf
    i = 0

    while(erro>e):
        r0 = r1
        if tipofunc == 1:
            c += 0.1
        else:
            if grau == 4:
                c+=0.1
            else:
                c += 0.3
        i+=1
        
        if grau == 2:
            r1 = gaussLegrende2Pontos(-c,c, a, b, e,tipofunc, tipoexp)
        elif grau==3:
            r1 = gaussLegrende3Pontos(-c,c, a, b, e,tipofunc, tipoexp)
        else:
            r1 = gaussLegrende4Pontos(-c,c, a, b, e,tipofunc, tipoexp)
        erro = fabs(r0-r1)
    print(f"Integral:{r1}")