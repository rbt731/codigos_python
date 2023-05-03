sexo = int(input("Digite seu sexo: (1)para homem, (2)para mulher: "))

if sexo == 1:
    ah = float(input("Digite sua altura: "))
    vh = 72.7*ah
    rh = vh - 58
    print(f"peso ideal para homem é {rh} Quilos.")
elif sexo == 2:
    am = float(input("Digite sua altura: "))
    vm = 62.1*am
    rm = vm - 44.7
    print(f"peso ideal para mulher é {rm} Quilos.")