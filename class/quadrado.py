class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudar_lado(self, novo_lado):
        print(f"LADO ANTIGO: {self.lado:.2f}")
        self.lado = novo_lado
        print(f"LADO ALTERADO: {novo_lado:.2f}")
        return novo_lado
    
    def area(self):
        area = self.lado * self.lado
        print(f"AREA: {area:.2f}")

quadrado1 = Quadrado(4)
quadrado1.area()
quadrado1.mudar_lado(6)
quadrado1.area()