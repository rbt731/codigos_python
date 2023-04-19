texto = "técnico em desenvolvimento de sistemas"
print("-=-=-=-=-=-=-=-=Título=-=-=-=-=-=-=-=-")
print("*"*10)
print(texto)

idade = int(input("informe sua idade: "))
print("#"*idade)

# Manipulando Texto(String)

print(f"o total de letras é {len(texto)}") # len() vem de length, que sinifica total

print(texto.lower()) # lower() coloca tudo em minuscolo
print(texto.upper()) # upper() coloca todo texto em maiúsculo
print(texto.capitalize()) # coloca a primeira letra em maiusculo
print(texto.replace("sistemas", "WEB")) # replace troca um texto por outro

# TRABALAHNDO com fatiamento

print("Fatiando a variavel texto")
print(texto[:3]) # vai exibir atodo o texto até a posição 2, a posição 3 não existe
print(texto[3:]) # vai exibir todo o texto a partir da posição 3
print(texto[3:10]) # vai exibir todo o texto que está na posição 3 até a 10