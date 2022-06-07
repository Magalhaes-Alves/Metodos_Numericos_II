import numpy as np
import metodospotencia


tamanhoMatriz = int(input("Insira o tamanho da matriz: "))
eps = float(input("Insira o erro: "))
M = np.zeros([tamanhoMatriz, tamanhoMatriz])
x = np.zeros([tamanhoMatriz, 1])

for i in range(tamanhoMatriz):
    M[i, :] = [float(j) for j in input("Insira a linha {} da matriz: ".format(i)).split(" ")]

for i in range(tamanhoMatriz):
    x[i, 0] = float(input("Insira a posição {} do vetor: ".format(i)))

(autoValor, autoVetor) = metodospotencia.metodoPotenciaInversa(M, x, eps)

print("Auto valor: {}\n\nAuto Vetor:\n{}".format(autoValor, autoVetor / autoVetor[2, 0]))
