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
            print("FILA NÃO ESTÁ CHEIA")
            return False
        
    def filaVazia(self):
        if self.elementos == 0:
            print("FILA VAZIA")
            return True
        else:
            print("FILA NÃO VAZIA")
            return False
        
    def enfileirar(self, valor):
        if self.filaCheia():
            print("ERRO DE FILA CHEIA")
            return
        if self.fim == self.capacidade - 1:
            self.fim = -1
        self.fim  = self.fim + 1
        self.valores[self.fim] = valor
        self.elementos = self.elementos + 1
    
    def desenfileirar(self):
        if self.filaVazia():
            print("ERRO DE FILA VAZIA")
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

fila = Fila(3)
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
print(fila.verPrimeiro())  
print(fila.desenfileirar())  
fila.enfileirar(40)
print(fila.verPrimeiro())
print("FILA: ", fila.valores)