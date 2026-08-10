print("Boletim de Notas")

nome = input ("Insira o nome do(a) aluno(a): ")
disciplina = input ("Insira a disciplina: ")
nota = float (input ("Nota do(a) aluno(a): "))

if (nota>= 60 and nota<=100) :
    print ("Aluno está APROVADO!")
elif (nota<40):
    print ("Aluno está REPROVADO!")
elif (nota>=40 and nota<60):
    print ("Aluno está em RECUPERAÇÃO!")
else:
    print ("Número digitado inválido")
