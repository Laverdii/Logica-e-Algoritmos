programa {
  funcao inicio() {
    escreva ("BOLETIM DE NOTAS")

    //Strings
    cadeia nome
    cadeia disciplina
    real nota
    cadeia status

    //Informações
    escreva ("\nNome do(a) aluno(a): ")
    leia (nome)

    escreva("\nDisciplina do(a) aluno(a): ")
    leia (disciplina)

    escreva ("\nInsira a nota do(a) aluno(a): ")
    leia (nota)

    //Condicionais
    se (nota>=60 e nota<=100) {
      escreva ("\nEstá APROVADO!")
    } senao se (nota<40) {
      escreva ("\nEstá REPROVADO!")
    } senao se (nota>=40 e nota<60) {
      escreva ("\nEstá de RECUPERAÇÃO!")
    } senao {
      escreva ("\nNúmero digitado inválido.")
    }
  }
}
