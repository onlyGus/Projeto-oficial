import sqlite3

#abertura de conexão e aquisição de cursor
banco = sqlite3.connect("academia.db")
cursor = banco.cursor()


#executando os comandos SQL
comando = ("DELETE FROM cadastro WHERE nome ='Gesse'")


cursor.execute(comando)

#efetivando o comando
banco.commit()

#fechamento das conexões
cursor.close()
banco.close()
