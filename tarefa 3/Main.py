from integracoes import integracao

print("Calculadora da Integral da função f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 pelas fórmulas de Newton-Cotes")

print("Menu")
print("0-Resposta pedida na tarefa 3")
print("1-Calcular a Integral da função por uma fórmula fechada")
print("2-Calcular a Integral da função por uma fórmula aberta")

opcao = input(("Digite a opção que você deseja:"))

if opcao == '0':
    print("Calculando a integral de f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de 0 a 1\n")

    print("-"*48)
    print("Calculando pelas fórmulas de Newton-Cotes fechadas")
    print("-"*48 + "\n")

    print("\n-Polinômio de substituição de grau 1 (Regra do Trapézio)")

    integracao(0,1, 0.0000001,1)

    print("\n-Polinômio de substituição de grau 2 (Regra de Simpson 1/3)")

    integracao(0,1, 0.0000001,2)

    print("\n-Polinômio de substituição de grau 3 (Regra de Simpson 3/8)")

    integracao(0,1, 0.0000001,3)

    print("\n-Polinômio de substituição de grau 4")

    integracao(0,1, 0.0000001,4)

    print("\n" + "-"*48)
    print("Calculando pelas fórmulas de Newton-Cotes abertas")
    print("-"*48 + "\n")

    print("\n-Polinômio de substituição de grau 1 (Regra do Trapézio Aberta)")

    integracao(0,1, 0.0000001, 1, True )

    print("\n-Polinômio de substituição de grau 2 (Fórmula de Milne)")

    integracao(0,1, 0.0000001, 2, True)

    print("\n-Polinômio de substituição de grau 3")

    integracao(0,1, 0.0000001, 3, True)

    print("\n-Polinômio de substituição de grau 4")

    integracao(0,1, 0.0000001, 4, True)
elif opcao == '1':
    limiteInferior = float(input("Digite o limite inferior da integral:"))
    
    limiteSuperior = float(input("Digite o limite superior da integral:"))

    grauErro = int(input("Digite o  grau do erro:"))

    erro = 1/(10**grauErro)

    grauPolinomio = int(input("Digite o grau do Polinômio de Substituição:"))

    print(f"Calculando a integral da função f(x)=f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de {limiteInferior} a {limiteSuperior}\n")

    print(f"\n-Polinômio de substituição de grau {grauPolinomio} com erro {erro}")

    integracao(limiteInferior,limiteSuperior,erro,grauPolinomio)
elif opcao == '2':
    limiteInferior = float(input("Digite o limite inferior da integral:"))
    
    limiteSuperior = float(input("Digite o limite superior da integral:"))

    grauErro = int(input("Digite o  grau do erro:"))

    erro = 1/(10**grauErro)

    grauPolinomio = int(input("Digite o grau do Polinômio de Substituição:"))

    print(f"Calculando a integral da função f(x)=f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de {limiteInferior} a {limiteSuperior}\n")

    print(f"\n-Polinômio de substituição de grau {grauPolinomio} com erro {erro}")

    integracao(limiteInferior,limiteSuperior,erro,grauPolinomio, True)
else:
    print("Você digitou uma opção inválida.")