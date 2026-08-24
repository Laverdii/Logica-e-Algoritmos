print("Promoção")
status = input("Você foi promovido sim ou não? ")
aceito = status.strip().lower() == "sim"
salario = float(input("Qual seu salário? "))
promocao = salario + (salario * 0.15)
if (status == "sim") :
  print(f"Você foi promovido e seu salario passou de {salario:.2f} para {promocao:.2f}.")
else :
  print(f"Você não foi promovido, então salário continua {salario:.2f}.")
