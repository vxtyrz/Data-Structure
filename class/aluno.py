class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        if self.nota1 >= 0 and self.nota2 >= 0:
            media = ((self.nota1 + self.nota2)/2)
            print(f"A média do aluno {self.nome} é: {media}")
            return media
        else:
            print("Notas inválidas")
            return None

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Nota 1: {self.nota1:.2f}, Nota 2: {self.nota2:.2f}")

    def aprovacao(self):
        media = self.calcular_media()
        if media is not None:
            if media >= 7:
                print(f"O aluno {self.nome} foi aprovado!")
            else:
                print(f"O aluno {self.nome} foi reprovado!")

aluno1 = Aluno("Vítor", 8, 6)
aluno1.exibir_dados()
aluno1.calcular_media()
aluno1.aprovacao()

aluno2 = Aluno("João", 5, 4)
aluno2.exibir_dados()
aluno2.calcular_media()
aluno2.aprovacao()
