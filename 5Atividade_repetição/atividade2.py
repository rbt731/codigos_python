valor = 50
soma = 0
somaHotel =0
for i in range(1,4):
    nome = input("Digite o nome do cliente: ")
    diaria = float(input("Informe a quantidade de diarias: "))
    if diaria < 15:
        soma = diaria * 4
        valorTotal = soma + valor
        print(f"Nome do cliente: {nome}.\nValor da conpra: R${valorTotal}.\n")
        somaHotel += valorTotal
    elif diaria == 15:
        soma = diaria * 3.60
        valorTotal = soma + valor
        print(f"Nome do cliente: {nome}.\nValor da conpra: R${valorTotal}.\n")
        somaHotel += valorTotal
    elif diaria > 15:
        soma = diaria * 3
        valorTotal = soma + valor
        print(f"Nome do cliente: {nome}.\nValor da conpra: R${valorTotal}.\n")
        somaHotel += valorTotal
print(f"{somaHotel}")