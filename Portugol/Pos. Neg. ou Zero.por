programa {
  funcao inicio() {
    escreva("Identificador de sinal\n")
    real num1
    escreva("Digite um número para saber qual seu sinal: ")
    leia(num1)
    se (num1 > 0) {
      escreva("Seu número é positivo")
    } senao se (num1 == 0) {
      escreva("Seu número é zero")
    } senao {
      escreva("Seu número é negativo")
    }
  }
}
