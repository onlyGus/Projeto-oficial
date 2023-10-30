import sqlite3

#abertura de conexão e aquisição de cursor
banco = sqlite3.connect("academia.db")
cursor = banco.cursor()


#executando os comandos SQL
comando = ("SELECT * FROM cadastro WHERE idade = 18")
cursor.execute(comando)

#obtendo os resultados da consulta
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)


#fechamento das conexões
cursor.close()
banco.close()
