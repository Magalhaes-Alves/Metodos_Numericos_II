import integracoes

print("\nCalculadora da Integral da função f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 pelas fórmulas de Newton-Cotes")

print("------------------------Menu---------------------------")
print("0-Calcular a Integral da função com quadratura de Gauss Lagrende com 2 pontos")
print("1-Calcular a Integral da função com quadratura de Gauss Lagrende com 3 pontos")
print("2-Calcular a Integral da função com quadratura de Gauss Lagrende com 4 pontos")
print("-------------------------------------------------------\n")
opcao = input(("Digite a opção que você deseja:"))


if opcao == '0':
    limiteInferior = float(input("\nDigite o limite inferior da integral:"))
    
    limiteSuperior = float(input("Digite o limite superior da integral:"))

    grauErro = int(input("Digite o  grau do erro:"))

    erro = 1/(10**grauErro)


    print(f"Calculando a integral da função f(x)=f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de {limiteInferior} a {limiteSuperior}\n")

    print(f"\n-Quadratura de Gauss Lagrende com 2 pontos com erro {erro}")

    integracoes.gaussLegrende2Pontos(limiteInferior,limiteSuperior,erro)

elif opcao == '1':
    limiteInferior = float(input("\nDigite o limite inferior da integral:"))
    
    limiteSuperior = float(input("Digite o limite superior da integral:"))

    grauErro = int(input("Digite o  grau do erro:"))

    erro = 1/(10**grauErro)


    print(f"Calculando a integral da função f(x)=f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de {limiteInferior} a {limiteSuperior}\n")

    print(f"\n-Quadratura de Gauss Lagrende com 3 pontos com erro {erro}")

    integracoes.gaussLegrende3Pontos(limiteInferior,limiteSuperior,erro)

elif opcao=='2':
    limiteInferior = float(input("\nDigite o limite inferior da integral:"))
    
    limiteSuperior = float(input("Digite o limite superior da integral:"))

    grauErro = int(input("Digite o  grau do erro:"))

    erro = 1/(10**grauErro)


    print(f"Calculando a integral da função f(x)=f(x)=(sin(2*x) + 4*(x**2) + 3*x)**2 de {limiteInferior} a {limiteSuperior}\n")

    print(f"\n-Quadratura de Gauss Lagrende com 4 pontos com erro {erro}")

    integracoes.gaussLegrende4Pontos(limiteInferior,limiteSuperior,erro)
else:
    print("Você digitou uma opção inválida.")
