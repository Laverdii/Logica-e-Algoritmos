programa {
  funcao inicio() {
    real a, b, definir
    
    escreva("Insira um número: ")
    leia(a)
    escreva("Insira um número: ")
    leia(b)

    escreva("Insira 1 para somar\nInsira 2 para subtrair\nInsira 3 para multiplicar\nInsira 4 para dividir\n")
    leia (definir)

    se (definir == 1) {
      real resultado = a + b
      escreva("O resultado é: ", resultado)
    } senao se (definir == 2) {
      real resultado = a - b
      escreva("O resultado é: ", resultado)
    } senao se (definir == 3) {
      real resultado = a * b
      escreva("O resultado é: ", resultado)
    } senao se (definir == 4) {
      real resultado = a / b
      escreva("O resultado é: ", resultado)
    } senao {
      escreva("Algo deu errado... Tente novamente.")
    }
  }
}
