salario = float(input("Digite o valor do seu salário: R$ "))

if salario < 600:
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    print("Seu salário sofrerá reajuste")
    print(f"R$ {(salario*0.3) + salario}")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

else:
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    print("Você não tem direito ao reajuste de salário.")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")