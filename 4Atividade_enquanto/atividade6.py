import os # importando biblioteca para trabalhar com sistemas operacional
dentroIntervalo = 0
foraIntervalo = 0
contador = 1
os.system("cls")
while contador <= 5:
    valor = int(input(f"Informe o valor {contador}: "))
    if valor >= 10 and valor <= 20:
        dentroIntervalo += 1
    else:
        foraIntervalo += 1
    contador += 1
print(f"valores dentro do intervlo: {dentroIntervalo}")
print(f"valores fora do intervlo: {foraIntervalo}")