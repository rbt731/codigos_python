percurso = int(input("Quantos quilometros foram percorridos: "))
carro = int(input("Informe o seu tipo de carro: "))

if carro == 3:
    gasA = percurso/12
    print(f"consome {gasA}km/litros de gasolina")
elif carro == 2:
    gasB = percurso/9
    print(f"consome {gasB}km/litros de gasolina")
elif carro == 1:
    gasC = percurso/8
    print(f"consome {gasC}km/litros de gasolina")