programa {
  funcao inicio() {
    real num1, num2, num3
    escreva("Maior entre 3 valores\n")
    escreva("Digite o primeiro valor: ")
    leia(num1)
    escreva("Digite o segundo valor: ")
    leia(num2)
    escreva("Digite o último valor: ")
    leia(num3)

    se (num1>num2 e num1>num3) {
      escreva("O maior entre os 3 é o primeiro, com valor de: ", num1)
    } senao se (num2>num1 e num2>num3) {
      escreva("O maior entre os 3 é o segundo, com valor de: ", num2)
    } senao {
      escreva("O maior entre os 3 é o terceiro, com valor de: ", num3)
    }
  }
}
