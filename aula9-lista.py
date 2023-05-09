notas = [9.5, 7.0, 6.5, 9.0]

print(notas)

print(type(notas))

for item in notas:
    print(item)

notas[2] = 8.5

print("$"*30)

print(notas)

# inserindo valores na lista
# 1º forma
notas.append(4) # vai inserir o item no final da lista
print(notas,"\n")
# 2º forma
notas.insert(1,10) # insert precisa de dois parametos. 1- é o valor índice que desejo inserir o valor. 2- éo valor propriamente dito que quero inserir
print(notas, "\n")

# removendo valores
# 1º forma
notas.pop()# exclui o ultimo elemento
print(notas, "\n")

# 2º forma
notas.pop(2) # removendo pelo índice
print(notas, "\n")

# 3º forma
notas.remove(9.5) # o remove() exclui usando o conteúdo da lista como parâmetro
print(notas, "\n")