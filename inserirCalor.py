import sqlite3

banco = sqlite3.connect("meu-banco.db")

cursor = banco.cursor ()

cursor.execute ("INSERT INTO alunos VALUES ('Carol', 202214, 'Carol43@gmail.com')")

banco.commit()