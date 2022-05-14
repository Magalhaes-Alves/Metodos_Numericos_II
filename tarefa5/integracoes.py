from math import sin, fabs, inf


def f(x):
    
    return (sin(2*x) + 4*(x**2) + 3*x)**2


def gaussLegrende2Pontos(a,b,e):

    iteracoes = 1
    n = 1

    xa1 = ((a + b) / 2) + ((b-a)/2)*(-0.577350269)
    xa2 = ((a + b) / 2) + ((b-a)/2)*(0.577350269)

    #w1=w2=1
    #Ro é a fórmula do somatório de f(x(alphak))wk
    integral_velha = ((b-a)/2)*( f(xa1)*1 + f(xa2)*1 )
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

            sum += ((delta)/2)*( f(xa1) + f(xa2) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    print(f'Partições:{n}')
    print(f'Integral encontrada: {integral_nova}')


def gaussLegrende3Pontos(a,b,e):

    iteracoes = 1
    n = 1
    xa1 = ((a + b) / 2) + ((b-a)/2)*(-0.774596669)
    #alpha1 = -raiz(3/5)
    xa2 = ((a + b) / 2)
    #alpha2 = 0
    xa3 = ((a + b) / 2) + ((b-a)/2)*(0.774596669)
    #alpha3 = raiz(3/5)

    #Ro é a fórmula do somatório de f(x(alphak))wk
    integral_velha = ((b-a)/2)*( f(xa1)*(5.0/9.0) + f(xa2)*(8.0/9.0) + f(xa3)*(5.0/9.0) )
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

            sum += ((delta)/2)*( f(xa1)*(5.0/9.0) + f(xa2)*(8.0/9.0) + f(xa3)*(5.0/9.0) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    print(f'Partições:{n}')
    print(f'Integral encontrada: {integral_nova}')


def gaussLegrende4Pontos(a,b,e):
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
    integral_velha = ((b-a)/2)*( f(xa1)*(0.3478548451) + f(xa2)*(0.6521451548) + f(xa3)*(0.6521451548) + f(xa4)*(0.3478548451) )
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

            sum += ((delta)/2)*( f(xa1)*(0.3478548451) + f(xa2)*(0.6521451548) + f(xa3)*(0.6521451548) + f(xa4)*(0.3478548451) )

            x0 += delta
        
        integral_nova = sum
        erro =fabs((integral_nova-integral_velha)/integral_nova)
    print(f'Partições:{n}')
    print(f'Integral encontrada: {integral_nova}')
