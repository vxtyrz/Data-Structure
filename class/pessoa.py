class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def enevelhecer(self, nova_idade):
        if nova_idade > self.idade:
            self.idade = nova_idade
            print(f"{self.nome} agora tem {self.idade} anos.")

    def emagrecer(self, peso_perdido):
        if peso_perdido > 0 and peso_perdido <= self.peso:
            self.peso -= peso_perdido
            print(f"{self.nome} agora pesa {self.peso} kg.")
        else:
            print("Peso perdido inválido.")
    
    def engordar(self, peso_ganho):
        if peso_ganho > 0:
            self.peso += peso_ganho
            print(f"{self.nome} agora pesa {self.peso} kg.")

    def crescer(self, altura_ganha):
        if self.idade < 21:
            altura_ganha = altura_ganha + 0.05
        else:  
            if altura_ganha > 0:
                self.altura += altura_ganha
                print(f"{self.nome} agora mede {self.altura} metros.")

pessoa1 = Pessoa("João", 20, 70, 1.75)
pessoa1.enevelhecer(22)
pessoa1.emagrecer(5)
pessoa1.engordar(3)
pessoa1.crescer(0.01)