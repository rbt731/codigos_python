lanche = ("pizza", "hotdog", "refri", "batata")
print(lanche)
print(type(lanche))# estou mostrando o tipo da variável

print(lanche[1])
print(f"o total de lanches é {len(lanche)}\n")

#lanche[2] = "suco"

for contador in range (0,4):
    print(lanche[contador])

print("#"*20)

for item in lanche:
    print(item)

print("#"*20)
# enumerate serve para permitir acessar os índices da tupla. Já a variável índice, irá armazenar os valores do índice
for indice,elemento in enumerate(lanche):
    print(f"{indice} = {elemento}")