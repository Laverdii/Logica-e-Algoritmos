print("Quem pode votar?")
idade = int(input("Digite sua idade: "))
t_eleitor = input("Tem título de eleitor: ")
aceito = t_eleitor.strip().lower() == "sim"

if (idade >= 16 and t_eleitor == "sim") :
  print(f"Com a idade de {idade}, e com seu título de eleitor regularizado, você pode votar!")
elif (idade < 16) :
  print(f"Com a idade de {idade}, você não pode votar.")
else : 
   print("Regularize seu titulo para votar!")
