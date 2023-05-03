a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))
d = int(input("Insira o 4º valor: "))

if a % 2 == 0:
    if a % 3 == 0:
        if a % 2 == 0 and a % 3 == 0:
            print(f"O valor {a} é divisível por 2 e por 3.\n")
        print(f"O valor {a} é divisível por 3.\n") 
    print(f"O valor {a} é divisível por 2.\n")

if b % 2 == 0:
    if b % 3 == 0:
        if b % 2 == 0 and a % 3 == 0:
            print(f"O valor {b} é divisível por 2 e por 3.\n")
        print(f"O valor {b} é divisível por 3.\n") 
    print(f"O valor {b} é divisível por 2.\n")
if c % 2 == 0:
    if c % 3 == 0:
        if c % 2 == 0 and a % 3 == 0:
            print(f"O valor {c} é divisível por 2 e por 3.\n")
        print(f"O valor {c} é divisível por 3.\n") 
    print(f"O valor {c} é divisível por 2.\n")

if d % 2 == 0:
    if d % 3 == 0:
        if d % 2 == 0 and a % 3 == 0:
            print(f"O valor {d} é divisível por 2 e por 3.\n")
        print(f"O valor {d} é divisível por 3.\n") 
    print(f"O valor {d} é divisível por 2.\n")
