from math import sqrt, pi, sin


def f(x):

    return (sin(2*x) + 4*(x**2) + 3*x)**2

def raizesPesos(n,tipo_gauss):
    
    if n == 2 and tipo_gauss =="h":
        return [
            [-1/sqrt(2),sqrt(pi)/2],
            [1/sqrt(2),sqrt(pi)/2]
        ]
    elif n==2 and tipo_gauss == "l":
        return [
            [2-sqrt(2),1/4*(2+sqrt(2))],
            [1/4*(2-sqrt(2)),1/4*(2-sqrt(2))]
        ]
    elif n==2 and tipo_gauss == "t":
        return [
            [-1/sqrt(2),pi/2],
            [1/sqrt(2),pi/2]
        ]
    elif n==3 and tipo_gauss == "h":
        return [
            [-sqrt(3/2),sqrt(pi)/6], 
            [0,2*sqrt(pi)/3],
            [sqrt(3/2),sqrt(pi)/6]
        ]
    elif n==3 and tipo_gauss == "l":
        return [
            [0.4157745568,0.7110930099], 
            [2.2942803603,0.2785177336],
            [6.2899450829,0.0103892565]
        ]
    elif n==3 and tipo_gauss == "t":
        return [
            [-(sqrt(3)/2),pi/3], 
            [0,pi/3],
            [sqrt(3)/2,pi/3]
        ]
    elif n==4 and tipo_gauss == "h":
        return [
            [-sqrt(3/2+sqrt(3/2)),sqrt(pi)/(4*(3+sqrt(6)))],
            [-sqrt(3/2-sqrt(3/2)),-sqrt(pi)/(4*(sqrt(6)-3))],
            [sqrt(3/2-sqrt(3/2)),-sqrt(pi)/(4*(sqrt(6)-3))],
            [sqrt(3/2+sqrt(3/2)),sqrt(pi)/(4*(3+sqrt(6)))]
        ]
    elif n==4 and tipo_gauss == "l":
        return [
            [0.32254768,0.60315426], 
            [1.74576110,0.35744186],
            [4.53662029,0.03888790],
            [9.39507091,0.00053929]
        ]
    elif n==4 and tipo_gauss == "t":
        return [
            [-1/2*sqrt(2+sqrt(2)),pi/4], 
            [-1/2*sqrt(2-sqrt(2)),pi/4],
            [1/2*sqrt(2-sqrt(2)),pi/4],
            [1/2*sqrt(2+sqrt(2)),pi/4]
        ]

def integracaoGaussHermite(n):
    integral = 0
    zeros_pesos = raizesPesos(n,"h")
    #print(zeros_pesos)
    for i in range(n):
        integral += zeros_pesos[i][1]*f(zeros_pesos[i][0])

    return integral

def integracaoGaussLaguerre(n):
    integral = 0
    zeros_pesos = raizesPesos(n,"l")
    #print(zeros_pesos)
    for i in range(n):
        integral += zeros_pesos[i][1]*f(zeros_pesos[i][0])

    return integral

def integracaoGaussChebyshev(n):
    integral = 0
    zeros_pesos = raizesPesos(n,"t")
    #print(zeros_pesos)
    for i in range(n):
        integral += zeros_pesos[i][1]*f(zeros_pesos[i][0])

    return integral

n= int(input("Digite o grau do polinomio:"))
print(f"Intergral Gauss-Hermite encontrada: {integracaoGaussHermite(n)}")
print(f"Intergral Gauss-Laguerre encontrada: {integracaoGaussLaguerre(n)}")
print(f"Intergral Gauss-Chebyshev encontrada: {integracaoGaussChebyshev(n)}")

