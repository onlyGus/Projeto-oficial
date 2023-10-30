import sqlite3

banco = sqlite3.connect("meu-banco.db")

cursor = banco.cursor ()

cursor.execute ("DELETE FROM alunos WHERE nome ='Daniela'")

banco.commit()