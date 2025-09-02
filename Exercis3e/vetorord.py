
class Valor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [0] * capacidade
        self.ultima_posicao = -1

    def inserir(self, valor):
        if self.ultima_posicao == (self.capacidade - 1):
            print("VETOR CHEIO")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def imprimir(self):
        if self.ultima_posicao == -1:
            print("VETOR VAZIO")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "-", self.valores[i])

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
        return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while limite_inferior <= limite_superior:
            posicao_atual = (limite_inferior + limite_superior) // 2
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif self.valores[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1

        return -1

    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            print(f"Valor {valor} não encontrado.")
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            print(f"Valor {valor} excluído da posição {posicao}.")
            return posicao
        
vetor = Valor(5)
vetor.inserir("V")
vetor.inserir("I")
vetor.inserir("T")
vetor.inserir("O")
vetor.inserir("R")
vetor.imprimir()
print("Antes de excluir")
vetor.excluir("I")
vetor.excluir("R")
vetor.excluir("V")
print("Depois de excluir")
vetor.imprimir()


            