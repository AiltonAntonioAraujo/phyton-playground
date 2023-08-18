import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INT NOT NULL);''')

def cria_aluno(nome, idade):
    conexao.execute("INSERT INTO aluno(nome, idade) VALUES (?,?);", (nome, idade))
    conexao.commit()
    print("Aluno cadastrado")

def listar_alunos():
    lista_alunos = conexao.execute("SELECT * FROM aluno;")
    for aluno in lista_alunos:
        print(aluno);

def atualizar_aluno(id, novo_nome, nova_idade):
    conexao.execute('''UPDATE aluno
                        SET nome = ?,
                            idade = ?
                        WHERE id = ?;''', (novo_nome,nova_idade,id))
    conexao.commit()
    print(f"Aluno atualizado: {novo_nome}")

def deletar_aluno(id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;", (id,))
    conexao.commit()
    print(f"Aluno {id} removido!")


#cria_aluno("João Francisco", 60)

#atualizar_aluno(1,"Lionora", 38)
listar_alunos()
deletar_aluno(3)
listar_alunos()
    
    


