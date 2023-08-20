import sqlite3

#Conectar no banco
conn = sqlite3.connect("praticedb.db")

#Criando banco de dados;
conn.execute('''CREATE TABLE IF NOT EXISTS pratice (
                 ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                 NOME NOT NULL,
                 DOCUMENTO NOT NULL  
                  );''')
conn.commit()
#Inserindo um registro#
pratice1_name="Ailton Antônio de Araújo"
pratice1_doc="4560789"
conn.execute('''INSERT INTO pratice (NOME, DOCUMENTO) 
                VALUES (?,?);''',
                (pratice1_name,pratice1_doc))
conn.commit()
#consultado dados no banco
rs = conn.execute('''SELECT NOME, DOCUMENTO FROM pratice WHERE ID = ?''',(1,))

for i in rs:
    print(i[0])
