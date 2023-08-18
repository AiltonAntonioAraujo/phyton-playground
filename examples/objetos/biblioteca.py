class Autor():
    def __init__(self, nome):
        self.nome = nome

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
        else: 
            print("O livro já foi emprestado")

    def devolver(self,):
        if self.emprestado == True:
            self.emprestado = False
        else:
            print("O Livro já foi devolvido")

class Usuario():
    def __init__(self, login):
        self.login = login


autor1 = Autor("Wes Mckinney")
livro1 = Livro("Python para analise de dados", autor1)

livro1.emprestar()

print(autor1.nome)
print(livro1.titulo)
print(livro1.emprestado)
livro1.emprestar()



