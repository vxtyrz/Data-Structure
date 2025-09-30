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
            self.ultimo = self.novo_no
        else:
            self.primeiro.anterior = self.novo_no
            self.novo_no.proximo = self.primeiro
            self.primeiro = self.novo_no

    def ins_final(self, valor):
        self.novo_no = No(valor)
        if self.lvazia():
            self.primeiro = self.novo_no
        else:
            self.ultimo.proximo = self.novo_no
            self.novo_no.anterior = self.ultimo
        self.ultimo = self.novo_no

    def excl_inicio(self):
        