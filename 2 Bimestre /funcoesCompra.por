programa {
  funcao formaPagamento(inteiro forma){
    se(forma == 1) {
      escreva("A forma de pagamento será no cartão de crédito.")
    } senao se(forma == 2) {
      escreva("A forma de pagamento será no cartão de débito.")
    } senao se(forma == 3) {
      escreva("A forma de pagamento será no PIX.")
    } senao se(forma == 4) {
      escreva("A forma de pagamento será no dinheiro")
    }
  }

  funcao descontoProgressivo(inteiro forma, real valor) {
    real desconto
    se((forma == 3 ou forma == 4) e valor >= 100 e valor < 300) {
      desconto = valor * 0.10
      valor -= desconto
      escreva("Com o desconto de ", desconto, "(10%) o valor final da compra será: ", valor) 
    } senao se((forma == 3 ou forma == 4) e valor >= 300 e valor < 500) {
      desconto = valor * 0.15
      valor -= desconto
      escreva("Com o desconto de ", desconto, "(15%) o valor final da compra será: ", valor) 
    } senao se((forma == 3 ou forma == 4) e valor >=500) {
      desconto = valor * 0.20
      valor -= desconto
      escreva("Com o desconto de ", desconto, "(20%) o valor final da compra será: ", valor) 
    } senao {
      escreva("Nenhum desconto a ser aplicado, valor da compra continua sendo: ", valor)
    }
  }

  funcao inicio() {
    inteiro forma
    real valor

    escreva("\nDigite o valor da sua compra: ")
    leia(valor)
    
    escreva("Qual forma de pagamento desejada?\n")
    escreva("[1] Cartão de crédito\n")
    escreva("[2] Cartão de débito\n")
    escreva("[3] PIX\n")
    escreva("[4] Dinheiro\n")
    leia(forma)
    formaPagamento(forma)

    descontoProgressivo(forma, valor)
  }
}
