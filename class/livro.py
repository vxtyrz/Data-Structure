class Livro:
    def __init__(self, titulo, autor, paginas, status):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.status = status
    
    def emprestimo(self):
        if self.emprestimo:
            return False
        self.emprestado = True
        return True
    
    def devolver(self):
        self.emprestado = False

    def esta_disponivel(self):
        return not self.emprestado