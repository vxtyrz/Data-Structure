class Conta:
    def __init__(self, numero, saldo = 0):
        self.saldo = saldo
        self.numero = numero

    def resumo(self):
        print("CC N°: {} Saldo: R${}".format(self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def depósito(self, valor):
        self.saldo += valor

minha_conta = Conta(32587023857, 2000)
minha_conta.resumo()
minha_conta.saque(800)
minha_conta.resumo()
minha_conta.depósito(500)
minha_conta.resumo()