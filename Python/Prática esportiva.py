print("Prática esportiva")

idade = int(input("Digite sua idade: "))
autorizacao = input("Você tem autorização: ").lower().strip()

if (idade >= 12 and idade <= 18 and autorizacao == "sim") :
  print("Está liberado para praticas esportivas")
else :
  print("Não está liberado!")
