valor = []
par = 0
impar = 0
for i in range(1,11):
    valor.append(i)
for a in range(0,10):
    if valor[a] % 2 == 0:
        par += 1
    else:
        impar += 1
print(valor, "\n")
print(f"O total de números pares é {par}. \n")
print(f"O total de números impares é {impar}. \n")