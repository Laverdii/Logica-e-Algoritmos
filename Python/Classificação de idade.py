print("Classificação de idade")

idade int(input("Digite sua idade: "))

if (idade <= 12) :
  print("Você é classificado como uma criança!")
elif (idade >= 12 and idade < 18) :
  print("Você é classificado como um adolescente!")
elif (idade >= 18 and idade < 60) :
  print("Você é classificado como um adulto!")
else :
  print("Você é classificado como um idoso")
