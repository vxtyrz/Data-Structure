class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def mostrar_lista(self):
        if self.primeiro is None:
            print("LISTA VAZIA")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.primeiro is None:
            print("LISTA VAZIA")
            return
        self.primeiro = self.primeiro.proximo

    def pesquisar(self, valor):
        if self.primeiro is None:
            print("LISTA VAZIA")
            return False
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def excluir_qualquer(self, valor):
        if self.primeiro is None:
            print("LISTA VAZIA")
            return
        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return
        anterior = self.primeiro
        atual = self.primeiro.proximo
        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo


lista = ListaEncadeada()

for letra in "vitor":
    lista.inserir(letra)

print("Lista após inserção dos caracteres:")
lista.mostrar_lista()

lista.excluir_inicio()
print("\nLista após exclusão do primeiro elemento:")
lista.mostrar_lista()

resultado_pesquisa = lista.pesquisar("r")
print(f"\nPesquisa pelo caractere 'r': {'Encontrado' if resultado_pesquisa else 'Não encontrado'}")

lista.excluir_qualquer("t")
print("\nLista após exclusão do elemento 't':")
lista.mostrar_lista()
