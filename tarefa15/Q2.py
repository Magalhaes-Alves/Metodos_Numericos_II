import numpy as np


def dividir_dominio(yi,yf,deltaX,N):
    x = yi
    y = yi
    e = np.zeros((N-1,N-1,2))
    for j in range(1,N):
        for k in range(1,N):
            e[j-1][k-1][0] = x + j * deltaX
            e[j-1][k-1][1] = y + k * deltaX
    return e;    

  
def preencherMatriz(matriz, n, deltaX, deltaY):
    eq = -1
    for l in range(n - 1):
        for c in range(n - 1):
            eq += 1
            matriz[eq][eq] = - 2*(1/(deltaX**2)+1/(deltaY**2))
            if c > 0:
                matriz[eq][eq - 1] = 1/(deltaX**2)
            if c < n - 2:
                matriz[eq][eq + 1] = 1/(deltaX**2)
            if l > 0:
                matriz[eq][eq - (n - 1)] = 1/(deltaX**2)
            if l < n - 2:
                matriz[eq][eq + (n - 1)] = 1/(deltaX**2)

    return matriz

def PVC2():
    N = 8
    yi = 0
    yf = 1
    deltaX = abs(yf-yi)/N
    deltaY = abs(yf-yi)/N

    dominio = dividir_dominio(yi,yf,deltaX,N)    
    print('Dominio: ')
    print(dominio)

    #produzindo a matriz A
    A = np.zeros((((N-1)**2),((N-1)**2)))   

    A = preencherMatriz(A, N, deltaX, deltaY)

    print('Matriz:')
    print(A)

    B = np.zeros((N-1)**2)
    for j in range(len(B)):
        B[j] = 4

    print('B:')
    print(B)    

    print("X:")
    X = np.linalg.solve(A, B)
    print(X)

    #Array exato pegue na aula 27 para calcular os erros.
    vetorExato = [-0.171875, -0.21875, -0.171875, -0.21875, -0.28125, -0.21875, -0.171875, -0.21875, -0.171875]

    vetorObtido = [X[8],X[10],X[12],X[22],X[24],X[26],X[36],X[38],X[40]]

    erro = []
    for exato, obtido in zip(vetorExato, vetorObtido):
        erro.append((exato - obtido)/obtido)

    