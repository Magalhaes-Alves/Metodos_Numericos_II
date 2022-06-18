import numpy as np
from math import sqrt, atan, cos, sin

def metodoHouseHolder(matrizA):
    n = matrizA.shape[0]
    H = np.identity(n)
    # Esta matriz vai ser passada para o método de Jacobi ou QR para recuperar os autovetores da matriz original.
    Ai_1 = matrizA
    for i in range(n-2):
        #Construção da matriz de Householder do passo i
        Hi = construcaoMatrizHouseholder(Ai_1,i,n)

        #Transformação de similaridade do passo i
        inter = np.dot(Hi.transpose(),Ai_1)
        resultado = np.dot(inter, Hi)
        Ai = np.around(resultado,5)

        #Salvar para o próximo passo.
        Ai_1 = Ai 

        #Acumular o produto das matrizes de Householder
        H = np.dot(H, Hi)

    return (Ai, H)


def construcaoMatrizHouseholder(matrizA, i, n):
    w = np.zeros(n)
    wLinha = np.zeros(n)

    # Copiar os elementos abaixo da diagonal da coluna i da matriz A para as respectivas posições no vetor w, isto é, da posição i+1 até o final.
    w[(i+1):n] = matrizA[(i+1):n,i]
    
    #Calcular o comprimento do vetor w
    lw = sqrt(np.add.reduce(w*w))
    
    #Copiar lw na posição i+1 do vetor wlinha
    wLinha[i+1] = lw
   
    #Calcular o vetor N
    N = w - wLinha
  
    #Normalizar o vetor N
    Nnormalizado = N / (sqrt(np.add.reduce(N*N)))
    
    #Montar a matriz de Householder
    
    Ntransposta = np.array([Nnormalizado])
    H = np.identity(n) - 2*Nnormalizado*(Ntransposta.transpose())

    return H


def matrizJacobiBaseadaNoElementoIJ(A, i, j, n):
    eps = 0.000001
    Jij = np.identity(n)

    if abs(A[i,j]) <= eps:
        #Considerar Aij = 0, retorna a matriz identidade
        return Jij
    
    if abs(A[i,i] - A[j,j]) <=eps:
        teta = np.pi/4
    else:
        teta = (1/2)*atan((-2*A[i,j])/(A[i,i]-A[j,j]))
        #Esta função já retorna um ângulo +/- 
        # no primeiro quadrante sentido anti-horário (+) 
        # no primeiro quadrante sentido horário (-)
    
    Jij[i,i] = cos(teta)
    Jij[j,j] = cos(teta)
    Jij[i,j] = sin(teta)
    Jij[j,i] = -sin(teta)

    return Jij
    

def varreduraDeJacobi(A, n):
    J = np.identity(n)
    #Esta matriz contém os produtos das matrizes ortogonais Jij para recuperar os autovetores da matriz original.
    Avelha = A

    for j in range(n-1):
        for i in range(j+1,n):
            #Construção da matriz de Jacobi Jij
            Jij = matrizJacobiBaseadaNoElementoIJ(Avelha, i, j, n)

            #Transformação de similaridade do passo ij
            # Produto de três matrizes.
            # Como Jij não é simétrica, sua transposta (Jij)T precisa ser computada
            inter = np.dot(Jij.transpose(),Avelha)
            Anova = np.dot(inter, Jij)

            Avelha = Anova

            #Acumular o produto das matrizes de Jacobi
            J = np.dot(J, Jij)
    #No final do loop externo, o formato da matriz Anova já está mais próximo do formato de uma matriz diagonal.
    return (Anova, J)
    

def metodoJacobi(A, eps):
    n = A.shape[0]

    P = np.identity(n)
    Avelha = A
    val = 100
    #Escalar ao qual é atribuída a soma dos quadrados dos elementos abaixo da diagonal da matriz Anova para verificar convergência.

    while(val>eps):
        #Varredura de Jacobi (devolve uma matriz que deve se aproximar de uma matriz diagonal
        Anova, J = varreduraDeJacobi(Avelha,n)

        Avelha = Anova

        P = np.dot(P, J)

        #Verificar se a matriz Anova já é diagonal
        abaixo = np.tril(Anova) - np.diag(np.diag(Anova))
        val = np.sum(abaixo*abaixo)

    #Ao sair do loop, o formato da matriz Anova já está suficientemente próximo do formato de
    #uma matriz diagonal. Assim, os elementos da diagonal são os autovalores da matriz original
    #de entrada e as colunas de P são os autovetores correspondente.

    #Copia os elementos da diagonal da matriz no vetor Lamb
    lamb = np.diag(Anova) 
    
    return (P,lamb)


def matrizJacobiBaseadaNoElementoIJRvelha(A, i, j, n):
    eps = 0.000001

    Jij = np.identity(n)
    #Matriz identidade com n x n elementos

    if abs(A[i,j]) <= eps:
        #Considerar Aij = 0, retorna a matriz identidade
        return Jij
    #Calcular Teta
    if abs(A[j,j]) <= eps:
        if A[i,j] < 0:
            #O numerador será positivo e assumimos tangente tende a +Inf
            teta = np.pi/2
        else:
            #O numerador será negativo e assumimos tangente tende a -Inf
            teta = -np.pi/2
    else:
        #Esta função já retorna um ângulo +/-
        # no primeiro quadrante sentido anti-horário (+)
        # no primeiro quadrante sentido horário (-)
        teta = atan(-A[i,j]/A[j,j])

    Jij[i,i] = cos(teta)
    Jij[j,j] = cos(teta)
    Jij[i,j] = sin(teta)
    Jij[j,i] = -sin(teta)

    return Jij


def decomposicaoQR(A, n):
    #Esta matriz contém os produtos das matrizes ortogonais Jij
    QT = np.identity(n)
    
    #Na inicialização, Rvelha não tem a estrutura de uma matriz triangular superior
    Rvelha = A
    for j in range(n-1):
        for i in range(j+1,n):
            #Construção da matriz de Jacobi Jij
            Jij = matrizJacobiBaseadaNoElementoIJRvelha(Rvelha, i, j, n)
            
            #Matriz modificada com elemento (i,j) zerado
            Rnova = np.dot(Jij,Rvelha)

            Rvelha = Rnova
            #QT é a transposta de Q. Note a ordem do produto
            QT = np.dot(Jij, QT)

    #No final do loop externo, o formato da matriz Rnova é triangular superior.
    Q = QT.transpose()

    return (Q, Rnova)


def metodoQR(A, eps):
    n = A.shape[0]

    #Escalar ao qual é atribuída a soma dos quadrados dos elementos abaixo da diagonal da matriz Anova para verificar convergência.
    val = 100
    #Matriz que contém os produtos das matrizes ortogonais Q para recuperar os autovetores da matriz original.
    P = np.identity(n)
    Avelha = A
    cont = 1

    while(val > eps):
        #Decomposição QR(Devolve as matrizes Q e R tais que
        # Avelha = QR, onde Q é ortogonal e R é triangular superior)
        Q, R = decomposicaoQR(Avelha, n)

        #Calcular a nova matriz como Anova=RQ(na ordem reversa)
        Anova = np.dot(R, Q)
        #isso é equivalente a Qt.Avelha.Q (transformação de similaridade)

        Avelha = Anova

        P = np.dot(P, Q)

        #Verificar se a matriz Anova já é diagonal
        abaixo = np.tril(Anova) - np.diag(np.diag(Anova))
        val = np.sum(abaixo*abaixo)

        print(f"Matriz diagonal da iteração {cont}:\n{np.around(Anova,5)}\n")
        print(f"Matriz acumulada da iteração {cont}:\n{np.around(P,5)}\n")
        cont+=1
    #Ao sair do loop, o formato da matriz Anova já está suficientemente próximo do formato de
    # uma matriz diagonal. Assim, os elementos da diagonal são os autovalores da matriz original
    #de entrada e as colunas de P são os autovetores correspondente.
    
    #Copia os elementos da diagonal da matriz no vetor Lamb
    lamb = np.diag(Anova)

    return (P, lamb)


def metodoQRAlternativo(A, eps):
    n = A.shape[0]
    
    abarra, H = metodoHouseHolder(A)

    val = 100
    P = np.identity(n)
    Avelha = abarra
    cont = 1

    while(val > eps):
        Q, R = decomposicaoQR(Avelha, n)

        Anova = np.dot(R, Q)

        Avelha = Anova

        P = np.dot(P, Q)

        abaixo = np.tril(Anova) - np.diag(np.diag(Anova))
        val = np.sum(abaixo*abaixo)

        print(f"Matriz diagonal da iteração {cont}:\n{np.around(Anova,5)}\n")
        print(f"Matriz acumulada da iteração {cont}:\n{np.around(P,5)}\n")
        cont+=1

    lamb = np.diag(Anova)

    return (P, lamb, H)
