def exercicio1() :
  # EXERCÍCIOS 1, 2, 3, 4.
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
  
def exercicio5() :
  # 5.
  print("Dobro e Triplo")
  a = int(input("Digite um número para descobrir seu dobro e triplo: "))
  
  dobro = a * 2
  triplo = a * 3
  
  print(f"O dobro de {a} é: {dobro}\n")
  print (f"O triplo de {a} é: {triplo}")

def exercicio6() :
  # 6.
  print("Sucessor/Antecessor\n")
  num = int(input("Digite um número para saber seu sucessor e antecessor: "))
  
  sucessor = num + 1
  antecessor = num - 1
  
  print(f"O sucessor de {num} é: {sucessor}\nO antecessor de {num} é: {antecessor}")

def exercicio7() :
  # 7.
  print("Perímetro do retângulo")
  lado1 = float(input("Digite o comprimento do retângulo: "))
  lado2 = float(input("Digite a altura do retângulo: "))
  perimetro = (lado1 * 2) + (lado2 * 2)
  
  print(f"O perimetro do retângulo é: {perimetro}")

def exercicio8() :
  # 8.
  print("Área do triângulo")
  base = float(input("Digite a base do triângulo: "))
  altura = float(input("Digite a altura do triângulo: "))
  area = (base * altura) / 2
  print(f"A área do triângulo é: {area}")

def exercicio9() :
  # 9.
  print("Maior entre 2 números")
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  
  if num1 > num2 :
    print(f"O número {num1}, é maior que {num2}")
  else :
    print(f"O número {num2}, é maior que {num1}")

def exercicio10() :
  # 10.
  print("Identificador de paridade\n")
  num1 = float(input("Digite um número para descobrir sua paridade: "))
  
  if (num1 % 2 == 0) :
      print(f"O número {num1} é par")
  else :
      print(f"O número ", num1, " é ímpar")

def exercicio11() :
  # 11.
  print("Identificador de sinal\n")
  num1 = float(input("Digite um número para saber qual seu sinal: "))
  
  if (num1 > 0) :
    print("Seu número é positivo")
  elif (num1 == 0) :
    print("Seu número é zero")
  else :
    print("Seu número é negativo")

def exercicio12() :
    # 12.
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
        
def exercicio13() :
    # 13.
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

def exercicio14() :
    # 14.
    print("Desconto")
    produto = float(input("Qual o valor do seu produto? "))

    print("Você recebeu um desconto de 10%")
    desconto = 0.1

    precoFinal = produto - (produto * desconto)
    print(f"O valor total da sua compra após o desconto de 10%, foi de: {precoFinal:.2f}.")
    
def exercicio15() :
    # 15.
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

def exercicio16() :
    # 16.
    print("Promoção")
    status = input("Você foi promovido sim ou não? ")
    aceito = status.strip().lower() == "sim"
    salario = float(input("Qual seu salário? "))
    promocao = salario + (salario * 0.15)
    if (status == "sim") :
        print(f"Você foi promovido e seu salario passou de {salario:.2f} para {promocao:.2f}.")
    else :
        print(f"Você não foi promovido, então salário continua {salario:.2f}.")
    
def exercicio17() :
    # 17.
    print("Entrada de um evento: 18 anos e com ingresso")
    idade = int(input("Digite sua idade: "))
    ingresso = input("Você tem ingresso? ").lower().strip()

    if (idade >= 18 and ingresso == "sim") :
        print("Você está liberado entrar!")
    elif (idade < 18 and ingresso == "sim") :
        print("Você não pode entrar por ser menor de idade.")
    else :
        print("Compre um ingresso para entrar.")
        
def exercicio18() :
    # 18.
    print("Senha correta: cadastro + autenticação")
    cadastro = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    senha_autenticada = input(f"Sr. {cadastro}, digite sua senha: ")

    if (senha_autenticada == senha) :
        print("Cadastro realizado com sucesso!")
    else :
        print("Senha incorreta.")

def exercicio19() :
    # 19.
    print("Declaração de intervalo de 10 a 50")
    num = int(input("Digite um número para verificar se ele está entre 10 e 50: "))
    if (num >= 10 and num <= 50) :
        print("Está entre 10 e 50")
    else :
        print("Seu número não está entre 10 e 50.")

def exercicio20() :
    # 20.
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

def exercicio21() :
    # 21.
    print("Classificação de idade")

    idade = int(input("Digite sua idade: "))

    if (idade <= 12) :
        print("Você é classificado como uma criança!")
    elif (idade >= 12 and idade < 18) :
        print("Você é classificado como um adolescente!")
    elif (idade >= 18 and idade < 60) :
        print("Você é classificado como um adulto!")
    else :
        print("Você é classificado como um idoso")
        
def exercicio22() :
    # 22.
    print("Classificação de triângulo")

    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3) :
        print("Você tem um triângulo equilátero")
    elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3) :
        print("Você tem um triângulo escaleno")
    else :
        print("Você tem um triângulo isósceles")

def exercicio23() :
    # 23.
    print("Prática esportiva")

    idade = int(input("Digite sua idade: "))
    autorizacao = input("Você tem autorização: ").lower().strip()

    if (idade >= 12 and idade <= 18 and autorizacao == "sim") :
        print("Está liberado para praticas esportivas")
    else :
        print("Não está liberado!")

def exercicio24() :
    # 24.
    print("Está chovendo?")

    esta_chovendo = input("Está chovendo? (s/n): ").lower() == "s"

    if not esta_chovendo :
        print("Não está chovendo. Você pode sair sem guarda-chuva.")
    else :
        print("Está chovendo. Leve um guarda-chuva!")

def exercicio25() :
    # 25.
    print("Listas/Opções para forma de pagamento")
    print("Escolha a forma de pagamento: ")
    print("(1) DINHEIRO\n (2) CARTÃO\n (3) PIX\n (4) BOLETO")
    opcao_escolhida = int(input("Digite a forma de pagamento: "))

    def forma_pagamento(opcao):
        if opcao == 1:
            print("Forma de pagamento selecionada: DINHEIRO")
        elif opcao == 2:
            print("Forma de pagamento selecionada: CARTÃO")
        elif opcao == 3:
            print("Forma de pagamento selecionada: PIX")
        elif opcao == 4:
            print("Forma de pagamento selecionada: BOLETO")
        else:
            print("Forma de pagamento inválida!!!")

    forma_pagamento(opcao_escolhida)
    
def exercicio26() :
    # 26.
    print("Desconto progressivo: 100 = 10%; 300 = 15%; acima de 500 = 20%")
    preco = float(input("Digite o valor da compra: "))

    def desconto_progressivo(preco):
        if preco >= 100 and preco < 300:
            desconto = preco * 0.10
            preco = preco - desconto
            print("Você recebeu 10% de desconto")
            print(f"Valor final da compra: {preco}")
        elif preco >= 300 and preco < 500:
            desconto = preco * 0.15
            preco = preco - desconto
            print("Você recebeu 15% de desconto")
            print(f"Valor final da compra: {preco}")
        elif preco >= 500:
            desconto = preco * 0.20
            preco = preco - desconto
            print("Você recebeu 20% de desconto")
            print(f"Valor final da compra: {preco}")
        else:
            print("Você não recebeu desconto!")
            print(f"Valor da compra: {preco}")

    desconto_progressivo(preco)

exercicio = int(input("""
===== LISTA DE EXERCÍCIOS =====
1 - Calculadora (Exercícios 1, 2, 3, 4)
5 - Dobro e triplo
6 - Sucessor e antecessor
7 - Perímetro do retângulo
8 - Área do triângulo
9 - Maior entre 2 números
10 - Par ou ímpar
11 - Positivo, negativo ou zero
12 - Maior entre 3 valores
13 - Quem pode dirigir?
14 - Desconto
15 - Quem pode votar?
16 - Promoção
17 - Entrada em evento
18 - Autenticação
19 - Intervalo de 10 a 50
20 - Calculadora simples
21 - Classificação de idade
22 - Classificação de triângulo
23 - Prática esportiva
24 - Está chovendo?
25 - Forma de pagamento
26 - Desconto progressivo

Escolha o exercício: """))

match exercicio:
    case 1:
        exercicio1()
        pass

    case 5:
        exercicio5()
        pass

    case 6:
        exercicio6()
        pass

    case 7:
        exercicio7()
        pass

    case 8:
        exercicio8()
        pass

    case 9:
        exercicio9()
        pass

    case 10:
        exercicio10()
        pass

    case 11:
        exercicio11()
        pass

    case 12:
        exercicio12()
        pass

    case 13:
        exercicio13()
        pass

    case 14:
        exercicio14()
        pass

    case 15:
        exercicio15()
        pass

    case 16:
        exercicio16()
        pass

    case 17:
        exercicio17()
        pass

    case 18:
        exercicio18()
        pass

    case 19:
        exercicio19()
        pass

    case 20:
        exercicio20()
        pass

    case 21:
        exercicio21()
        pass

    case 22:
        exercicio22()
        pass

    case 23:
        exercicio23()
        pass

    case 24:
        exercicio24()
        pass

    case 25:
        exercicio25()
        pass

    case 26:
        exercicio26()
        pass

    case _:
        print("Exercício inválido!")
