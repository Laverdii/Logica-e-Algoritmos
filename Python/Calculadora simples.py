print("Calculadora simples")
print("Calcular dois números inteiros")

a = float(input("Insira um número inteiro: "))
b = float(input("Insira um número inteiro: "))

escolha = int(input("Insira 1 para somar\nInsira 2 para subtrair\nInsira 3 para multiplicar\nInsira 4 para dividir\nInsira 5 para resto\nInsira 6 para potência\n"))

if (escolha == 1) :
    resultado = a + b
    print(f"A soma de {a} + {b} é: {resultado}")
elif (escolha == 2) :
    resultado = a - b
    print(f"A subtração de {a} - {b} é: {resultado}")
elif (escolha == 3) :
    resultado = a * b
    print(f"A multiplicação de {a} * {b} é: {resultado}")
elif (escolha == 4) :
    resultado = a / b
    print(f"A divisão de {a} / {b} é: {resultado}")
elif (escolha == 5) :
    resultado =  a % b
    print(f"O resto da divisão de {a} % {b} é: {resultado}")
elif (escolha == 6) :
    resultado = a ** b
    print(f"A potência de {a} elevado à {b} é: {resultado}")
else :
    print("Algo deu errado... Tente novamente.")
