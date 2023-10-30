import tkinter as tk
from tkinter import filedialog
import sqlite3

def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    experiencias = text_experiencias.get("1.0", tk.END)
    linkedin = entry_linkedin.get()
    status_emprego = entry_status_emprego.get()
    expectativa_salarial = entry_expectativa_salarial.get()
    curriculo = curriculo_path.get()

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('dados_devs.db')
    cursor = conn.cursor()

    # Criar tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS desenvolvedores
                    (nome TEXT, idade INTEGER, cidade TEXT, estado TEXT,
                    telefone TEXT, email TEXT, experiencias TEXT, linkedin TEXT,
                    status_emprego TEXT, expectativa_salarial TEXT, curriculo_path TEXT)''')

    # Inserir dados na tabela
    cursor.execute("INSERT INTO desenvolvedores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, idade, cidade, estado, telefone, email, experiencias, linkedin,
                    status_emprego, expectativa_salarial, curriculo))
    
    # Commit e fechar conexão
    conn.commit()
    conn.close()

    # Limpar campos após submissão
    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_experiencias.delete("1.0", tk.END)
    entry_linkedin.delete(0, tk.END)
    entry_status_emprego.delete(0, tk.END)
    entry_expectativa_salarial.delete(0, tk.END)
    curriculo_path.set("")

def selecionar_curriculo():
    curriculo = filedialog.askopenfilename()
    curriculo_path.set(curriculo)

# Interface Gráfica para Desenvolvedor
app = tk.Tk()
app.title("Cadastro de Desenvolvedor")

# Elementos da interface
tk.Label(app, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(app)
entry_nome.grid(row=0, column=1)

tk.Label(app, text="Idade:").grid(row=1, column=0)
entry_idade = tk.Entry(app)
entry_idade.grid(row=1, column=1)

tk.Label(app, text="Cidade:").grid(row=2, column=0)
entry_cidade = tk.Entry(app)
entry_cidade.grid(row=2, column=1)

tk.Label(app, text="Estado:").grid(row=3, column=0)
entry_estado = tk.Entry(app)
entry_estado.grid(row=3, column=1)

tk.Label(app, text="Telefone:").grid(row=4, column=0)
entry_telefone = tk.Entry(app)
entry_telefone.grid(row=4, column=1)

tk.Label(app, text="Email:").grid(row=5, column=0)
entry_email = tk.Entry(app)
entry_email.grid(row=5, column=1)

tk.Label(app, text="Experiências:").grid(row=6, column=0)
text_experiencias = tk.Text(app, height=5, width=40)
text_experiencias.grid(row=6, column=1)

tk.Label(app, text="LinkedIn:").grid(row=7, column=0)
entry_linkedin = tk.Entry(app)
entry_linkedin.grid(row=7, column=1)

tk.Label(app, text="Status de Emprego:").grid(row=8, column=0)
entry_status_emprego = tk.Entry(app)
entry_status_emprego.grid(row=8, column=1)

tk.Label(app, text="Expectativa Salarial:").grid(row=9, column=0)
entry_expectativa_salarial = tk.Entry(app)
entry_expectativa_salarial.grid(row=9, column=1)

curriculo_path = tk.StringVar()
tk.Label(app, text="Currículo:").grid(row=10, column=0)
tk.Button(app, text="Selecionar Currículo", command=selecionar_curriculo).grid(row=10, column=1)
tk.Button(app, text="Salvar", command=salvar_dados).grid(row=11, column=0, columnspan=2)

app.mainloop()