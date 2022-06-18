import numpy as np
import metodosSimilaridade as ms
import metodospotencia as mp

"""

Tarefa da aula 20

"""

M = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]])
x = np.array([[1], [1], [1], [1], [1]])
eps = 0.000001


abarra, H = ms.metodoHouseHolder(M)
print('\n'+ '-'*50 + '\n')
print("1)")
print("i - Matriz tridiagonal Abarra:")
print(abarra)

print("\nii -A matriz acumulada H:")
print(H)


(autoValor, autoVetor) = mp.metodoPotenciaRegular(abarra, x, eps)
autovetor1 = np.dot(H,autoVetor)
autovalor1 = autoValor
print('\n'+ '-'*50 + '\n')
print("3)\nUsando os métodos da potência para encontrar os autovalores e autovetores de Abarra")
print('\n'+ '-'*50 + '\n')
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

(autoValor, autoVetor) = mp.metodoPotenciaDeslocamento(abarra, x, eps,30)
autovetor2 = np.dot(H,autoVetor)
autovalor2 = autoValor
print('\n'+ '-'*50 + '\n')
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

(autoValor, autoVetor) = mp.metodoPotenciaDeslocamento(abarra, x, eps,20)
autovetor3 = np.dot(H,autoVetor)
autovalor3 = autoValor
print('\n'+ '-'*50 + '\n')
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

(autoValor, autoVetor) = mp.metodoPotenciaDeslocamento(abarra, x, eps,10)
autovetor4 = np.dot(H,autoVetor)
autovalor4 = autoValor
print('\n'+ '-'*50 + '\n')
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

(autoValor, autoVetor) = mp.metodoPotenciaInversa(abarra, x, eps)
autovetor5 = np.dot(H,autoVetor)
autovalor5 = autoValor
print('\n'+ '-'*50 + '\n')
print(f"Auto valor: {autoValor}\n\nAuto Vetor:\n{autoVetor / autoVetor[2, 0]}\n")

print('\n'+ '-'*50 + '\n')
print("4)\nAutovetores da matriz A:")
print(f"Autovetor1:{autovetor1/autovetor1[2, 0]}\n")
print(f"Autovetor2:{autovetor2/autovetor2[2, 0]}\n")
print(f"Autovetor3:{autovetor3/autovetor3[2, 0]}\n")
print(f"Autovetor4:{autovetor4/autovetor4[2, 0]}\n")
print(f"Autovetor5:{autovetor5/autovetor5[2, 0]}\n")

#Como os espectros das matrizes são os mesmos, os autovalores de Abarra são os mesmos de A
print('\n'+ '-'*50 + '\n')
print("5)\nAutovalores da matriz A:")
print(f"Autovalor 1:{autovalor1}\n")
print(f"Autovalor 2:{autovalor2}\n")
print(f"Autovalor 3:{autovalor3}\n")
print(f"Autovalor 4:{autovalor4}\n")
print(f"Autovalor 5:{autovalor5}\n")


"""

Tarefa da aula 22

"""
print("""
    Tarefa da aula 22
    1)
""")
P, Abarra = ms.metodoQR(M, eps)

print(f"A Matriz acumulada P:{P}")

print(f"\nA diagonal da matriz diagonal Abarra:{Abarra}\n")

print(f"Autovalor 1:{Abarra[0]}")
print(f"Autovetor 1:{P[:,0]/P[2,0]}\n")

print(f"Autovalor 2:{Abarra[1]}")
print(f"Autovetor 2:{P[:,1]/P[2,1]}\n")

print(f"Autovalor 3:{Abarra[2]}")
print(f"Autovetor 3:{P[:,2]/P[2,2]}\n")

print(f"Autovalor 4:{Abarra[3]}")
print(f"Autovetor 4:{P[:,3]/P[2,3]}\n")

print(f"Autovalor 5:{Abarra[4]}")
print(f"Autovetor 5:{P[:,4]/P[2,4]}\n")

print("\nMostrando os Autovalores e Autovetores encontrados pelo método de jacobi:\n")
Pjacobi, Abarrajacobi = ms.metodoJacobi(M, eps)

print(f"Autovalor 1:{Abarrajacobi[0]}")
print(f"Autovetor 1:{Pjacobi[:,0]/Pjacobi[2,0]}\n")

print(f"Autovalor 2:{Abarrajacobi[1]}")
print(f"Autovetor 2:{Pjacobi[:,1]/Pjacobi[2,1]}\n")

print(f"Autovalor 3:{Abarrajacobi[2]}")
print(f"Autovetor 3:{Pjacobi[:,2]/Pjacobi[2,2]}\n")

print(f"Autovalor 4:{Abarrajacobi[3]}")
print(f"Autovetor 4:{Pjacobi[:,3]/Pjacobi[2,3]}\n")

print(f"Autovalor 5:{Abarrajacobi[4]}")
print(f"Autovetor 5:{Pjacobi[:,4]/Pjacobi[2,4]}\n")

print()

print("\n2)\n")
print("i-\nImprimindo Anova que sai de cada iteração de QR:\n")

Palternativo, AbarraAlternativo, Halternativo = ms.metodoQRAlternativo(M, eps)

print("Sim, os termos que eram zero deixaram de ser zero.")

print("ii-\n")
print(f"Matriz P correta:\n{P}\n")
print(f"Matriz P com QR alternativo:\n{Palternativo}\n")
print("As colunas de P não são os autovetores de A.")

print("iii-\n")
print("P=HP:\n")
print(np.dot(Halternativo,Palternativo))