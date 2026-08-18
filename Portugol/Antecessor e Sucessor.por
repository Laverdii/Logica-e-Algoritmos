programa {
  funcao inicio() {
    inteiro a, antecessor, sucessor
    escreva ("Digite um número para descobrir seu sucessor e antecessor: ")
    leia(a)

    sucessor = a + 1
    escreva("O sucessor de ", a, " é: ", sucessor, "\n")

    antecessor = a - 1
    escreva("O antecessor de ", a, " é: ", antecessor)
  }
}
