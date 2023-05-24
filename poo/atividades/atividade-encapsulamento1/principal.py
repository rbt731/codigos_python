from calculadora import Calculadora
c1 = float(input("n1: "))
c2 = float(input("n2: "))
r = Calculadora(c1, c2)

print(f"Os valores inseridos são {c1} e {c2}, a soma deles é {r.soma()}")
r.subtrair()
print(f"Os valores inseridos são {c1} e {c2}, a multiplicação deles é {r.multi()}")
print(f"Os valores inseridos são {c1} e {c2}, a divisão deles é {r.divi()}")