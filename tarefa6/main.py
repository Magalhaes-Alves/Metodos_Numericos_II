from integracoes import integracaoGaussEspecial

print("|"+50*"-*"+"|")
print("Quadraturas especiais de Gauss".center(102,"-"))
print("|"+50*"-*"+"|")


grau_polinomio = int(input("Digite o grau n do polinomio(n:[2,4]):"))
print("\nf(x) = (sin(2*x) + 4*(x**2) + 3*x)**2\n")
opcao= str(input("Digite em qual integracao a funcao acima será aplicada.\n"
                 "h-> Gauss-Hermite\n"
                 "l-> Gauss-Laguerre\n"
                 "t-> Gauss-Chebyshev\n"
                 "\nDigite sua opcao:"))

if(opcao=="h"):
    print(f"Intergral Gauss-Hermite encontrada:{integracaoGaussEspecial(grau_polinomio,opcao)}")
elif(opcao=="l"):
    print(f"Intergral Gauss-Laguerre encontrada:{integracaoGaussEspecial(grau_polinomio,opcao)}")
elif(opcao=="t"):
    print(f"Intergral Gauss-Chebyshev encontrada: {integracaoGaussEspecial(grau_polinomio,opcao)}")
else:
    print("Essa nao eh uma opcao valida.")