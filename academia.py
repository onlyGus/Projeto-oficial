import sqlite3


#abertura de conexão e aquisição de cursor
banco = sqlite3.connect("academia.db")
cursor = banco.cursor()


#executando os comandos SQL
comando = '''CREATE TABLE cadastro(
            nome TEXT NOT NULL,
            texto TEXT NOT NULL,
            idade INTEGER NOT NULL 
            );'''

comando1 = ("INSERT INTO cadastro VALUES ('Gus', 'aluno', '27')")
comando2 = ("INSERT INTO cadastro VALUES ('Gesse', 'Professor', '30')")
comando3 = ("INSERT INTO cadastro VALUES ('Luana', 'aluna', '30')")
comando4 = ("INSERT INTO cadastro VALUES ('Marcelo', 'aluno', '30')")


cursor.execute(comando)
cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(comando3)
cursor.execute(comando4)

#efetivando o comando
banco.commit()

#fechamento das conexões
cursor.close()
banco.close()
