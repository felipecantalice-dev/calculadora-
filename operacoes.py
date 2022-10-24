from dataclasses import dataclass

@dataclass
class Operacao:
  n1: int
  n2: int

  def calcular(self) -> str:
    pass

  
  

class Soma(Operacao):
  def calcular(self) -> int:
    return self.n1 + self.n2


class Subtracao(Operacao):
  def calcular(self) -> int:
    return self.n1 - self.n2


class Multiplicacao(Operacao):
  def calcular(self) -> int:
    return self.n1 * self.n2


class Divisao(Operacao):
  def calcular(self) -> int:
    return self.n1 / self.n2
