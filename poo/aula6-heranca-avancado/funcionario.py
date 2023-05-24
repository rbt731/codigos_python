class Funcionario:
    def __init__(self,cargo,nome):
        self._cargo = cargo # esses dados estão com apenas 1 underline protegidos
        self._nome = nome
    def informacoes(self):
        print(f"Olá {self._nome} seu cargo atual é {self._cargo}\n")

class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario):
        super().__init__(cargo, nome)
        self._salario = salario
    def info(self):
        print(f"Olá {self._nome} seu cargo atual é {self._salario}\n")