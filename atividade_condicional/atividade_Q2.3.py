salario = int(input("Digite o vaor do seu salário: R$ "))

if salario < 600:
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    print("Seu salário sofrerá reajuste")
    print(f"R$ {salario*1.3}")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

if salario >= 600:
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    print("Você não tem direito ao reajuste de salário.")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")