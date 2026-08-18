print("Maior entre 3 valores\n")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o último valor: "))
if (num1>num2 and num1>num3) :
    print(f"O maior entre os 3 é o primeiro, com valor de: {num1}")
elif (num2>num1 and num2>num3) :
    print(f"O maior entre os 3 é o segundo, com valor de: {num2}")
else :
    print(f"O maior entre os 3 é o terceiro, com valor de: {num3}")
