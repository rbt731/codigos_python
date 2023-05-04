import os
soma = 0
valor = 1
os.system("cls")
while valor <= 4:
    num = int(input(f"Digite valor {valor}: "))
    soma = soma + num
    valor = valor + 1
media = soma / 4
print(f"sua média é {media}")
