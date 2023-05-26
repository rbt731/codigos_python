class Veiculos:
    def __init__(self, marca, ano):
        self._marca = marca
        self._ano = ano
    
    @property
    def marca(self):
        print(f"Marca do veículo: {self._marca}")
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def ano(self):
        print(f"ano do veículo: {self._ano}")
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

class Carro(Veiculos):
    def __init__(self, marca, ano, porta, mala):
        super().__init__(marca, ano)
        self.__porta = porta
        self.__mala = mala
    
    @property
    def porta(self):
        print(f"Nome do veículo{self.__porta}")
    
    @porta.setter
    def porta(self, porta):
        self.__porta = porta

    @property
    def mala(self):
        print(f"Nome do veículo{self.__mala}")
    
    @mala.setter
    def mala(self, mala):
        self.__mala = mala