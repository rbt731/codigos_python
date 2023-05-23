from conta import Conta
minhaConta = Conta(123, "Robervaldo Maganhães", 20000)
#minhaConta.relatorio()
minhaConta.saldo = 80500
minhaConta.meuSaldo()

print("Seu limite é ", minhaConta.getlimite())
minhaConta.setlimite(1400)

print("Seu limite é ", minhaConta.getlimite())
