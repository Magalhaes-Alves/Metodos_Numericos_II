import metodospotencia
import numpy as np

eps = 0.000001


M1 = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
x1 = np.array([[1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaRegular(M1, x1, eps)

print("Primeira matriz:[4, 2, 1], [1, 6, 2], [0, 1, 5]\n")
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M1 = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
x1 = np.array([[1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaDeslocamento(M1, x1, eps,2)

print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M1 = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
x1 = np.array([[1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaInversa(M1, x1, eps)

print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

#Segunda matriz


M2 = [[-14, 1, -2], [1, -1, 1], [-2, 1, -11]]
x2 = [1, 1, 1]

(autoValor, autoVetor) = metodospotencia.metodoPotenciaRegularAlternativo(M2, x2, eps)

aux = autoVetor[2]
for i in range(len(autoVetor)):
    autoVetor[i] = autoVetor[i]/aux

print('\n'+ '-'*50 + '\n')
print("Segunda matriz:[-14, 1, -2], [1, -1, 1], [-2, 1, -11]]\n")
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor}\n")

M2 = np.array([[-14, 1, -2], [1, -1, 1], [-2, 1, -11]])
x2 = np.array([[1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaDeslocamento(M2, x2, eps,-10)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M2 = np.array([[-14, 1, -2], [1, -1, 1], [-2, 1, -11]])
x2 = np.array([[1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaInversa(M2, x2, eps)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")


M3 = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x3 = np.array([[1], [1], [1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaRegular(M3, x3, eps)

print('\n'+ '-'*50 + '\n')
print("Terceira matriz:[40, 8, 4, 2, 1], [8, 30, 12, 6, 2]")
print("[4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]\n")

print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M3 = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x3 = np.array([[1], [1], [1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaDeslocamento(M3, x3, eps,30)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M3 = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x3 = np.array([[1], [1], [1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaDeslocamento(M3, x3, eps,20)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M3 = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x3 = np.array([[1], [1], [1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaDeslocamento(M3, x3, eps,10)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

M3 = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x3 = np.array([[1], [1], [1], [1], [1]])

(autoValor, autoVetor) = metodospotencia.metodoPotenciaInversa(M3, x3, eps)
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")
