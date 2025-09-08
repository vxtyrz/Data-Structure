class ContaCorrente:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente ou valor inválido")
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            print("Valor inválido para depósito")
            return False
        
    def transferir(self, valor, origem, destino):
        if self.saldo > valor and valor > 0:
            origem.sacar(valor)
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
            return True
        else:
            print("Saldo insuficiente ou valor inválido para transferência")
            return False
        
minha_conta = ContaCorrente(123456, "Vítor", 3000)
conta_amiga = ContaCorrente(654321, "João", 1000)
minha_conta.transferir(500, minha_conta, conta_amiga)
print(f"Saldo da minha conta: R${minha_conta.saldo:.2f}")