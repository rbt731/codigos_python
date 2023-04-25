lata = int(input("Digite quantas latas de 300ml quer: "))
garrafaA = int(input("Digite as garrafas de 600ml quer: "))
garrafaB = int(input("Digite as garrafas de 2l quer: "))

compraA = lata*300
compraB = garrafaA*600
compraC = garrafaB*2000
compratotal = (compraA/1000)+(compraB/1000)+(compraC/1000)
print("=-=-=-=-=-=-=-=-=Garrafas=-=-=-=-=-=-=-=-=")
print(f"Você comprou no total de {lata} lata de 300ml.")
print(f"Você comprou no total de {garrafaA} lata de 600ml.")
print(f"Você comprou no total de {garrafaB} lata de 2L.")
print(f"{compraA/1000}L, {compraB/1000}L, {compraC/1000}L.")
print("#=#=#=#=#=#Litros Refrigerante#=#=#=#=#=#=#")
print(f"Você tem no total de {compratotal} L de refrigerantes.")