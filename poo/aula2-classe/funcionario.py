class Funcionario:

    def __init__(self, nome, cargo, salario):
        # estamos criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passsar os parâmentros que serão usados como valores dos atributos da classe
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Olá {self.nome} seu cargo é {self.cargo} seu salário é {self.salario}")

