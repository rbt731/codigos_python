import random
from random import randint
import os

os.system("cls")
sorteio = [] #criando uma lista
for i in range(1,7):
    sorteio.append(randint(1,100))
#valor = randint(1,100) # essa função irá gerar um número aleatorio
print(sorteio)
sorteio.sort()
print(sorteio)
sorteio.sort(reverse=True)
print(sorteio)
os.system("pause")# ira pausar o sistema até uma tecla ser precionada