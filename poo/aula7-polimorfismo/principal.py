from produto import Produto, Livro, Eletronico

l1 = Livro("piriri", 123, "pororo")
e1 = Eletronico("v", 2000, "m")

l1.descrever()
l1.calcularPreco()
e1.calcularPreco()