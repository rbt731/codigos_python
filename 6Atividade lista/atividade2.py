vet = []
i = 10
posi = 0
while i <= 20:
    vet.append(i)
    i += 1
for a in range(1,10):
    if vet[a] == 10:
        posi = 1
print(f"{posi} {vet[posi]}")