maior = 0
menor = 0
soma = 0
soma1 = 0
s = 0
i = 0 
while i <= 6:
    altura = float(input("Informe sua altura: "))
    sexo = int(input("Informe seu sexo: "))
    if i == 0:
        menor = altura
    else:
        if altura >= maior:
            maior = altura
        if altura <= menor:
            menor = altura
    if sexo == 2:
        soma += altura
        s += 1
    soma1 += altura
    mediatotal = soma1 / 6
    i += 1
mediaM = soma / s
print(maior)
print(menor)
print(mediaM)