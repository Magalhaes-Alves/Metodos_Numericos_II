import metodospotencia

eps = 0.000001

M1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]
x1 = [1,1,1]

(autoValor, autoVetor) = metodospotencia.metodoPotencia(M1, x1, eps)

print("Primeira matriz:\n")
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor}")

M2 = [[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2],
 [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]]
x2 = [1,1,1,1,1]

(autoValor2, autoVetor2) = metodospotencia.metodoPotencia(M2, x2, eps)

print("\n\nSegunda Matriz:\n")
print(f"Auto valor: {autoValor2}\n\nAuto Vetor:\n{autoVetor2}")
