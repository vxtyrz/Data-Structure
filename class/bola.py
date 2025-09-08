class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor
        print("TROCAR")

    def mostra_cor(self):
        print(f"A cor da bola é: {self.cor}")

bola1 = Bola("Vermelha", 30, "Couro")
bola1.mostra_cor()
bola1.troca_cor("Azul")
bola1.mostra_cor()