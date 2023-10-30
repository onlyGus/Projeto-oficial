import sqlite3

banco = sqlite3.connect("meu-banco.db")

cursor = banco.cursor ()

cursor.execute ("CREATE TABLE alunos (nome text, matricula interger, email text)")

cursor.execute ("INSERT INTO alunos VALUES ('Daniela', 202212, 'daniela23@gmail.com')")
cursor.execute ("INSERT INTO alunos VALUES ('Fernando', 202213, 'ferando33@gmail.com')")

cursor.execute ("INSERT INTO alunos VALUES ('Carol', 202214, 'Carol43@gmail.com')")

banco.commit()

