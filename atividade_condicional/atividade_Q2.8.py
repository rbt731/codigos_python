a = float(input("Digite o lado 1: "))
b = float(input("Digite o lado 2: "))
c = float(input("Digite o lado 3: "))

if a < b + c and b < a + c and c < b + a:
    print("Pode formar um triangulo")
else:
    print("Não podem formar um triagulo")