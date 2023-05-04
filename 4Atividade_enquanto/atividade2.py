maior = 0

while True:
    num = int(input("Insira um valor: "))
    if num >= maior:
        maior = num
    if num == 0:
        break
print(f"o número maior é {maior}\n")
"""
num = 1
while num != 0:
    if num >= maior:
        maior = num
"""