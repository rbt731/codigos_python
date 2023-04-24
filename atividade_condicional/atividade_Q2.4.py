salario = float(input("Digite o valor do seu salário: R$ "))
financiamento = float(input("Qual o valor do financiamento: R$ "))
limite = financiamento * 5

if limite <= salario:
    print("Financiamento Concedido\n")
else:
    print("Financiamento Negado\n")

print("Obrigado por nos consultar\n")