class valor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [0] * capacidade
        self.ultima_posicao = -1

    def inserir(self, valor):
        if self.ultima_posicao == (self.capacidade - 1):
            print("O vetor atingiu a sua capacidade máxima")
        else:
            self.ultima_posicao = self.ultima_posicao + 1
            self.valores[self.ultima_posicao] = valor

    def imprimir(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "-", self.valores[i])
    
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                print("Valor", valor, "encontrado na posição", i)
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return posicao
        
vetor = valor(5)
vetor.inserir("V")
vetor.inserir("I")
vetor.inserir("T")
vetor.inserir("O")
vetor.inserir("R")
print("Antes de excluir")
vetor.imprimir()
vetor.pesquisar("T")
vetor.pesquisar("I")
vetor.pesquisar("R")
vetor.excluir("V")
vetor.excluir("T")
vetor.excluir("R")
print("Depois de excluir")
vetor.imprimir()