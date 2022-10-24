from operacoes import Operacao, Soma, Subtracao, Multiplicacao, Divisao


def Factory(n1: int = 0, n2: int = 0, op: str = '+') -> Operacao:

  operacao = {
    "+": Soma(n1, n2),
    "-": Subtracao(n1, n2),
    "*": Multiplicacao(n1, n2),
    "/": Divisao(n1, n2)
  }
  return operacao[op]


resultado = 0
n1: int = int(input("Digite o primeiro valor: "))
n2: int = int(input("Digite o segundo valor: "))

op: str = input("Digite uma das 4 operação matematica(+, -, *, /): ")

calculadora: Operacao = Factory(n1, n2, op)
print(calculadora.calcular())
