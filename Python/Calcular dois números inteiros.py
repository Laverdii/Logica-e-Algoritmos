print("Calcular dois números inteiros")

a = float(input("Insira um número inteiro: "))
b = float(input("Insira um número inteiro: "))

escolha = int(input("Insira 1 para somar\nInsira 2 para subtrair\nInsira 3 para multiplicar\nInsira 4 para dividir\n"))

if (escolha == 1) :
    resultado = a + b
    print(f"O resultado é: {resultado}")
elif (escolha == 2) :
    resultado = a - b
    print(f"O resultado é: {resultado}")
elif (escolha == 3) :
    resultado = a * b
    print(f"O resultado é: {resultado}")
elif (escolha == 4) :
    resultado = a / b
    print(f"O resultado é: {resultado}")
else :
    print("Algo deu errado... Tente novamente.")
