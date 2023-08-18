class Pessoa():
    #####  Sempre tem o parâmetro Self ##########
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

#####  realização de herança do objeto pessoa ##########
class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, titulo):
        #####  Chama o costrutor pai ##########
        super().__init__(nome, idade, sexo)
        self.titulo = titulo

    def info(self):
        print(f"O titulo é: {self.titulo}")


pessoa1 = Pessoa("Ailton","40","Masculino")
pessoa2 = Pessoa("Leonardo","44","Masculino")
pessoa3 = Pessoa("Leonora","38","Feminino")

pessoa1.saudacao()
pessoa2.saudacao()
pessoa3.saudacao()

professor1 = Professor("Manoel","50","Masculino","Doutor")
print(professor1.nome)
professor1.saudacao()
professor1.info()