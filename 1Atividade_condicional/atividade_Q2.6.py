percurso = float(input("Quantos quilometros foram percorridos: "))
carro = int(input("Informe o seu tipo de carro, 1, 2 ou 3: "))

if carro == 3:
    gas = percurso / 12
    #print(f"Tipo do carro é {carro} e vai precisar de {gas} litros de gasolina\n")

elif carro == 2:
    gas = percurso / 9
    #print(f"Tipo do carro é {carro} e vai precisar de {gas} litros de gasolina\n")

elif carro == 1:
    gas = percurso / 8
    #print(f"Tipo do carro é {carro} e vai precisar de {gas} litros de gasolina\n")

print(f"Tipo do carro é {carro} e vai precisar de {gas} litros de gasolina\n")