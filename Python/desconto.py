print("Desconto")
produto = float(input("Qual o valor do seu produto? "))

print("Você recebeu um desconto de 10%")
desconto = 0.1

precoFinal = produto - (produto * desconto)
print(f"O valor total da sua compra após o desconto de 10%, foi de: {precoFinal:.2f}.")
