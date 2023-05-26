from personagem import Personagem, Jogador
raca = input("Escolha sua raça: ")
if raca == "Goblin":
    h = "aa"
elif raca == "Humano":
    h = "bb"
j1 = Jogador("aaaa", raca)
j1.jog()
j1.usarHabilidade(h)