import integracoes
from math import pi


print("\nCalculadora de Integral")
print("------------------------Menu---------------------------")
print("1 - f(x)=1 / pow(pow(x, 2.0), (1 / 3.0)) de -1 a 1")
print("2 - f(x)=1 / pow(4 - (x * x), 0.5) de -2 a 0")

tipofunc = int(input("Digite a função que você deseja calcular a integral:"))

if tipofunc == 1:
    limiteInferior = -1
    limiteSuperior = 1
else:
    limiteInferior = -2
    limiteSuperior = 0

print("\nModos de Calcular")
print("1 - Por exponencial simples")
print("2 - Por exponencial dupla")

tipoexp = int(input("Digite o modo que você deseja calcular a integral:"))

print("\nMétodos depois da solução de Variável")
print("1 - Newton-Cotes Fechada")
print("2 - Newton-Cotes Aberta")
print("3 - Gauss-Legrende")

metodo = int(input("Digite o método a ser usado após a mudança de variável:"))

print("\nQuantos pontos você deseja usar?(Até 4 pontos)")
grau = int(input("Digite a quantidade de pontos a ser usado:"))

if tipofunc==2:
    erro = 0.00001
else:
    erro = 0.001

if metodo == 1:
    integracoes.integrarNewtonCotes(limiteInferior,limiteSuperior,erro,grau,tipofunc,tipoexp)
elif metodo == 2:
    integracoes.integrarNewtonCotes(limiteInferior,limiteSuperior,erro,grau,tipofunc,tipoexp,True)
else:
    integracoes.integrarGaussLegrende(limiteInferior,limiteSuperior,erro,grau,tipofunc,tipoexp)
