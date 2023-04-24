a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a < b + c and b < a + c and c < a + c:
    print("Pode formar um triangulo\n")
else:
    print("Não podem formar um triagulo\n")