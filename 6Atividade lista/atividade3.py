vet = []
for i in range(1,6):
    vet.append(int(input(f"Informe o número {i}: ")))

vet.sort(reverse=True)
print(vet)