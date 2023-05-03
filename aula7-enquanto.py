
contador = 1
while contador <=10:
    print(contador)
    contador = contador + 1

#while funcionando como loop condicional
"""
senha = ""
while senha != "123":
    senha = input("Informe sua senha: ")

print("Obrigado por usar o sistema\n")
"""
#while como se fosse o faça - enquanto
while True: 
    senha = input("informe sua senha: ")
    if senha == "123":
        break
    else:
        print("Senha errada, digite novamente.\n")
print("obrigado")