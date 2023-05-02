inicial = int(input("Informe o valor inicial: "))
final = int(input("Informe o valor final: "))
soma = 0
for cont in range(inicial,final + 1):
    soma = soma + cont

print(f"a soma de {inicial} + {final} é {soma}\n")