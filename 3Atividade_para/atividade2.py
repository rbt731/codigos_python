cont = 0
for valor in range(1,6):
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        cont = cont + 1
print(f"o total de maiores de 18: {cont}")