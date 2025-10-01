class No:
    def __init__(self, valor, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior

    def mostra_no(self):
        print(self.valor)

class LDE:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lvazia(self):
        return self.primeiro is None
    
    def inserir(self, valor):
        novo_no = No(valor)
        if self.lvazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.primeiro.anterior = novo_no
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no

    def ins_final(self, valor):
        novo_no = No(valor)
        if self.lvazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            novo_no.anterior = self.ultimo
        self.ultimo = novo_no

    def excl_inicio(self):
        if self.lvazia():
            return None
        temp = self.primeiro
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        return temp

    def excl_final(self):
        if self.lvazia():
            return None
        temp = self.ultimo
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        return temp


    def excl_qualquer(self, valor):
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            atual = atual.proximo
        if atual is None:
            return None
        if atual == self.primeiro:
            return self.excl_inicio()
        elif atual == self.ultimo:
            return self.excl_final()
        else:
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_lista(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return atual
            atual = atual.proximo
        return None

lista = LDE()
for letra in "VITOR":
    lista.inserir(letra)

print("Lista após inserção:")
lista.mostrar_lista()

removido = lista.excl_inicio()
print("Elemento removido:", removido.valor if removido else "Nenhum")

print("Lista após exclusão do primeiro:")
lista.mostrar_lista()

resultado = lista.buscar("O")
print("Busca pelo último caractere:", "Encontrado" if resultado else "Não encontrado")

removido = lista.excl_qualquer("A")
print("Elemento 'A' removido:", removido.valor if removido else "Não encontrado")


