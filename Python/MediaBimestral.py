import sys

print("Boletim de Notas")

nome = input("Nome do(a) aluno(a): ")
curso = input("Curso: ")
semestre = input("Semestre: ")
disciplina = input("Disciplina: ")
nota1 = int(input("Nota do primeiro bimestre: "))
nota2 = int(input("Nota do segundo bimestre: "))
media = (nota1 + nota2)/2

if (nota1>100 or nota1<0 or nota2>100 or nota2<0 or media>200 or media<0) :
    print("Algo deu errado... Tente novamente.")
    sys.exit(1)

if (media>=60 and media<=100) :
    status = "Aprovado!"
elif (media<40 and media>0) :
    status = "Reprovado!"
elif (media>=40 and media<60) :
    status = "Recuperação!"
else :
    print("Algo deu errado... Tente novamente.")
    sys.exit(1)

print(f"\nO aluno(a) {nome} do curso de {curso} que está cursando o {semestre} semestre na disciplina de {disciplina} obteve uma média de {media} e está com status: {status}")
