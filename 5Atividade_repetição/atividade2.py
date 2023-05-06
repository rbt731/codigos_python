soma = 0
somaHotel =0
for i in range(1,9):
    nome = input("Digite o nome do cliente: ")
    diaria = float(input("Informe a quantidade de diarias: "))
    valorTotal = diaria * 50
    if diaria < 15:
        soma = diaria * 4

    elif diaria == 15:
        soma = diaria * 3.60

    elif diaria > 15:
        soma = diaria * 3

    print(f"Olá {nome} você ficou {diaria} dias e vai pagar R${valorTotal+soma}")
    somaHotel += valorTotal
print(f"O hotel ira receber um total de: {somaHotel}")