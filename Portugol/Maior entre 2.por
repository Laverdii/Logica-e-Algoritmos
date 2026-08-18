programa {
  funcao inicio() {
    real num1, num2
    escreva("Maior entre 3 valores\n")
    escreva("Digite o primeiro valor: ")
    leia(num1)
    escreva("Digite o segundo valor: ")
    leia(num2)

    se (num1>num2) {
      escreva("O maior entre os 2 é o primeiro, com valor de: ", num1)
    } senao se (num2>num1) {
      escreva("O maior entre os 2 é o segundo, com valor de: ", num2)
    } senao {
      escreva("Algo deu errado... Tente novamente.")
    }
  }
}
