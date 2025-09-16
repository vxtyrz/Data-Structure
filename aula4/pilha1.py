class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = capacidade * [0]

    def pilhaCheia(self):
        if self.topo == self.capacidade - 1:
            print("PILHA CHEIA")
            return True
        else:
            print("PILHA NÃO ESTÁ CHEIA")
            return False
            
    def empilhar(self, valor):
        if self.pilhaCheia() == True:
            print("IMPOSSÍVEL EMPILHAR")
        else:
            self.topo = self.topo + 1
            self.valores[self.topo] = valor
            print(f"Valor {valor} empilhado com sucesso")

    def verTopo(self):
        if self.topo == -1:
            print("PILHA VAZIA")
            return None
        else:
            print("O topo da pilha é: ", self.valores[self.topo])

    def pilhaVazia(self):
        if self.topo == -1:
            print("PILHA VAZIA")
            return True
        else:
            print("PILHA NÃO VAZIA")
            return False
        
    def desempilhar(self):
        if self.pilhaVazia() == True:
            print("IMPOSSÍVEL DESEMPILHAR")
        else:
            self.valor = self.valores[self.topo]
            self.topo = self.topo - 1
            print("O valor desempilhado é: ", self.valor)
            return self.valor

pilha1 = Pilha(5)
pilha1.empilhar(10)
pilha1.empilhar(20)
pilha1.empilhar(30)
pilha1.empilhar(40)
pilha1.verTopo()
pilha1.desempilhar()
pilha1.verTopo()


