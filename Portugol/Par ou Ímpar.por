programa {
  funcao inicio() {
    escreva("Identificador de paridade\n")
    real num1
    escreva("Digite um número para descobrir sua paridade: ")
    leia(num1)
    se (num1 % 2 == 0) {
      escreva("O número ", num1, " é par")
    } senao {
      escreva("O número ", num1, " é ímpar")
    }
    }
}
