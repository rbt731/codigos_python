class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero # em python tornamos um elemento privado com 2 underlines. 1 underline ele está protegido, com nenhum underline ele está público
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite# esse atributo possui um valor padrão de forma que o usuario poderá ou não informar este valor
    
    def relatorio(self):
        print(f"Olá {self.__titular}, o número da sua conta é {self.__numero} e o seu saldo atual é R$ {self.__saldo} e o seu limite é R$ {self.__limite}")
    
    def meuSaldo(self):
        print(f"Olá {self.__titular}, seu saldo é R$ {self.__saldo}")

    # o método get irá retornar ou exibir o valor do atributo
    def getlimite(self):
        return self.__limite
    
    # o método set irá alterar o conteúdo do atributo, sem exibir nada
    def setlimite(self, valor):
        if valor < 0:
            print("valor menor que 0, infore outro valor")
        else:
            self.__limite = valor

    # VAMOS MODIFICAR O ATRIBUTO SALDO COM O @PROPERTY E @SETTER
    @property
    def saldo(self):
        print(f"Olá, seu saldo é {self.__saldo}\n")

    @saldo.setter
    def saldo(self, i):
        if i <= 0:
            print("Você não pode inserir valores menores ou igual zero\n")
        else:
            self.__saldo = i
    