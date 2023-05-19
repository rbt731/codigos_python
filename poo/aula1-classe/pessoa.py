class Pessoa:
    # atributos
    nome = "Fulano"
    idade = 30
    altura = 1.65
    #metodo
    def falar(self, texto): # self é um parâmetro obrigatorio do python que informa que o metodo pertence à própria classe que foi criada
        print(texto)
pessoa1 = Pessoa()
print(pessoa1.nome, pessoa1.idade)# instanciar é cria um objeto a partir de uma classe.
pessoa1.falar("Olá mundo")