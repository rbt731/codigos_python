valor = int(input("Informe um valor qualquer: "))
for cont in range(1, valor+1):
    if (valor % cont == 0):
        print(cont)