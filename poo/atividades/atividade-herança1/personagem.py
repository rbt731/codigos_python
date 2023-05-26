class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._vida = 3
    def atacar(self):
        print(f"Você está atacando")
    
class Jogador(Personagem):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.__raca = raca
    def jog(self):
        print(f"Olá player {self._nome}, sua raça é {self.__raca}")
    def usarHabilidade(self, poder):
        self.__raca = poder
        print(f"habilidade ativada: {self.__raca}")