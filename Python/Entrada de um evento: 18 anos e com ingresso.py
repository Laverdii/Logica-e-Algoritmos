print("Entrada de um evento: 18 anos e com ingresso")
idade = int(input("Digite sua idade: "))
ingresso = input("Você tem ingresso? ").lower().strip()

if (idade >= 18 and ingresso == "sim") :
  print("Você está liberado entrar!")
elif (idade < 18 and ingresso == "sim") :
  print("Você não pode entrar por ser menor de idade.")
else :
  print("Compre um ingresso para entrar.")
