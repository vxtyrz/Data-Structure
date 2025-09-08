class Retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura

    def mudar_valor(self, nova_largura, nova_altura):
        self.largura = nova_largura
        self.altura = nova_altura
        print(f"Os antigos valores eram: largura = {self.largura:.2f} e altura = {self.altura:.2f}")
        print(f'Os novos valores são: largura = {self.largura:.2f} e altura = {self.altura:.2f}')
        return self.largura, self.altura
    
    def area(self):
        area = self.largura * self.altura
        print(f'A área do retângulo é: {area:.2f}')
        return area

    def perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        print(f'O perímetro do retângulo é: {perimetro:.2f}')
        return perimetro
    
retangulo1 = Retangulo(5, 10)
retangulo1.mudar_valor(7, 14)
retangulo1.area()
retangulo1.perimetro()