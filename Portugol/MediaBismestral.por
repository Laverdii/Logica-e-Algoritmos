programa {
  funcao inicio() {
    cadeia semestre
    cadeia nome
    cadeia curso
    cadeia disciplina
    cadeia status
    inteiro nota1
    inteiro nota2
    inteiro media
 
    escreva("Boletim de Notas")

    escreva ("\nInsira o nome do(a) aluno(a): ")
    leia(nome)
    escreva ("Insira o curso: ")
    leia (curso)
    escreva ("Insira o semestre em que está: ")
    leia (semestre)
    escreva ("Insira a disciplina à consultar: ")
    leia (disciplina)
    escreva ("Insira a nota do primeiro bimestre: ")
    leia (nota1)
    escreva ("Insira a nota do segundo bimestre: ")
    leia (nota2)

    media = (nota1+nota2)/2

    se (nota1>100 ou nota1<0 ou nota2>100 ou nota2<0 ou media>200 ou media<0) {
     escreva ("\nAlgo deu errado... Tente novamente.")
     retorne
    }
    
    se (media>=60 e media<=100) {
     status ="Aprovado"
    } senao se (media<40 e media>=0) {
     status ="Reprovado"
    } senao se (media>=40 e media<60) {
     status ="Exame"
    } senao {
     escreva("\nAlgo deu errado... Tente novamente.")
     retorne
    }
   
   escreva("\nO aluno(a) ", nome, " do curso de ", curso, " que está cursando o ", semestre, " semestre ", "na disciplina de ", disciplina, " obteve uma média de ", media, " e está com status: ", status)
  }
}
