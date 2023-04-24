salario = int(input("Digite o valor do seu salário: R$ "))
financiamento = int(input("Insira o valor do financiamento pretendido: R$ "))
limite = salario*5

if financiamento <= limite:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")

print("Obrigado por nos consultar")