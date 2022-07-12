import numpy as np
import math


def dividir_dominio(yi,yf,deltaX,N):
    e = np.zeros(N-1)
    for j in range(1,N):
        e[j-1] = yi + j * deltaX
    return e;    

def solucao_exata(dominio):
    r = np.zeros(len(dominio))
    for j in range(len(r)):
        r[j] = (1/((math.e**(-1))-math.e))*((math.e**(-dominio[j]))-(math.e**(dominio[j])))
    return r

def derivada_segunda(dominio,deltaX):
    r = (1/(deltaX**2))*dominio[0] - (2/(deltaX**2)+1)*dominio[1] + (1/(deltaX**2)*dominio)[2]
    return r
    
def PVC1():
    N = 8
    yi = 0
    yf = 1
    deltaX = abs(yf-yi)/N


    dominio = dividir_dominio(yi,yf,deltaX,N)    
    print(f'Dominio:\n{dominio}')

    A = np.array([[- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0,0,0],
    [(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0,0],
    [0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0],
    [0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0],
    [0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0],
    [0,0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2))],
    [0,0,0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1)]])
    print('Matriz:')
    print(A)

    B = np.array([0,0,0,0,0,0,-(1/(deltaX**2))])
    print('B:')
    print(B)

    print("X:")
    X = np.linalg.solve(A, B)
    print(X)

    solucao = solucao_exata(dominio)
    print('Solução:')
    print(solucao) 

    erro = np.copy(X).astype('float')
    for p in range (len(X)):
        erro[p]= math.fabs(X[p]-solucao[p])/X[p]
    print('Erro relativo:')
    print(erro) 

