while True:
    num = int(input("Informe um valor de 1 a 9: "))
    
    if num % 2 == 0:
        for i in range(1,11):
            print(f"{num} x {i} = {num*i}")
    else:
        for i in range(1,11):
            print(f"{num} + {i} = {num+i}")
    if num == 0:
        break