print("Quem pode dirigir?")
idade = int(input("Digite sua idade: "))
cnh = input("Tem CNH: ")
aceito = cnh.strip().lower() == "sim"

if (idade >= 18 and cnh == "sim") :
  print(f"Com a idade de {idade}, e CNH regularizada, você pode dirigir!")
elif (idade < 18) :
  print(f"Com a idade de {idade}, você não pode dirigir.")
else : 
   print("Regularize sua CNH para dirigir!")
