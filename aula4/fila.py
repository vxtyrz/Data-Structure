class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.elementos = 0
        self.valores = capacidade * [0]

    def filaCheia(self):
        if self.elementos == self.capacidade:
            print("FILA CHEIA")
            return True
        else:
            return False
        
    def filaVazia(self):
        if self.elementos == 0:
            print("FILA VAZIA")
            return True
        else:
            return False
        
    def enfileirar(self, valor):
        if self.filaCheia():
            print("TENTATIVA DE ENFILEIRAR NOVO ELEMENTO: ERRO DE FILA CHEIA")
            return
        if self.fim == self.capacidade - 1:
            self.fim = -1
        self.fim  = self.fim + 1
        self.valores[self.fim] = valor
        self.elementos = self.elementos + 1
    
    def desenfileirar(self):
        if self.filaVazia():
            print("TENTATIVA DE DESENFILEIRAR: ERRO DE FILA VAZIA")
            return
        temp = self.valores[self.inicio]
        self.inicio = self.inicio + 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.elementos = self.elementos - 1
        return temp


    def verPrimeiro(self):
        if self.filaVazia():
            print("ERRO DE FILA VAZIA")
            return
        return self.valores[self.inicio]

fila = Fila(5)
fila.desenfileirar()
fila.enfileirar("V")
fila.enfileirar("Í")
fila.enfileirar("T")
fila.enfileirar("O")
fila.enfileirar("R")
fila.enfileirar("!")
print("PRIMEIRO ELEMENTO: ", fila.verPrimeiro())  
print("FILA: ", fila.valores)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
print("PRIMEIRO ELEMENTO: ", fila.verPrimeiro())
