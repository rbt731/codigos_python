from veiculo import Veiculos, Carro

marca = input("Informe a marca do veículo: ")
ano = int(input("Informe o ano do veículo: "))

v1 = Veiculos(marca, ano)

v1.marca
v1.ano

porta = int(input("Informe o total de portas do carro: "))
mala = int(input("Informe o total de porta malas do carro: "))

c1 = Carro(marca, ano, porta, mala)

c1.porta
c1.mala