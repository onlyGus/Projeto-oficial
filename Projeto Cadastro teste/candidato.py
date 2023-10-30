import tkinter as tk
from tkinter import filedialog
import sqlite3
 
class CandidatoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Desenvolvedor")
 
        tk.Label(self.master, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=0, column=1)
 
        tk.Label(self.master, text="Idade:").grid(row=1, column=0)
        self.entry_idade = tk.Entry(self.master)
        self.entry_idade.grid(row=1, column=1)
 
        tk.Label(self.master, text="Cidade:").grid(row=2, column=0)
        self.entry_cidade = tk.Entry(self.master)
        self.entry_cidade.grid(row=2, column=1)
 
        tk.Label(self.master, text="Estado:").grid(row=3, column=0)
        self.entry_estado = tk.Entry(self.master)
        self.entry_estado.grid(row=3, column=1)
 
        tk.Label(self.master, text="Telefone:").grid(row=4, column=0)
        self.entry_telefone = tk.Entry(self.master)
        self.entry_telefone.grid(row=4, column=1)
 
        tk.Label(self.master, text="Email:").grid(row=5, column=0)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=5, column=1)
 
        tk.Label(self.master, text="Experiências:").grid(row=6, column=0)
        self.text_experiencias = tk.Text(self.master, height=5, width=40)
        self.text_experiencias.grid(row=6, column=1)
 
        tk.Label(self.master, text="LinkedIn:").grid(row=7, column=0)
        self.entry_linkedin = tk.Entry(self.master)
        self.entry_linkedin.grid(row=7, column=1)
 
        tk.Label(self.master, text="Status de Emprego:").grid(row=8, column=0)
        self.entry_status_emprego = tk.Entry(self.master)
        self.entry_status_emprego.grid(row=8, column=1)
 
        tk.Label(self.master, text="Expectativa Salarial:").grid(row=9, column=0)
        self.entry_expectativa_salarial = tk.Entry(self.master)
        self.entry_expectativa_salarial.grid(row=9, column=1)
 
        self.curriculo_path = tk.StringVar()
        tk.Label(self.master, text="Currículo:").grid(row=10, column=0)
        tk.Button(self.master, text="Selecionar Currículo", command=self.selecionar_curriculo).grid(row=10, column=1)
        tk.Button(self.master, text="Salvar", command=self.salvar_dados).grid(row=11, column=0, columnspan=2)
 
    def salvar_dados(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        cidade = self.entry_cidade.get()
        estado = self.entry_estado.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        experiencias = self.text_experiencias.get("1.0", tk.END)
        linkedin = self.entry_linkedin.get()
        status_emprego = self.entry_status_emprego.get()
        expectativa_salarial = self.entry_expectativa_salarial.get()
        curriculo = self.curriculo_path.get()
 
        conn = sqlite3.connect('dados_devs.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS desenvolvedores
                        (nome TEXT, idade INTEGER, cidade TEXT, estado TEXT,
                        telefone TEXT, email TEXT, experiencias TEXT, linkedin TEXT,
                        status_emprego TEXT, expectativa_salarial TEXT, curriculo_path TEXT)''')
 
        cursor.execute("INSERT INTO desenvolvedores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (nome, idade, cidade, estado, telefone, email, experiencias, linkedin,
                        status_emprego, expectativa_salarial, curriculo))
 
        conn.commit()
        conn.close()
 
        self.limpar_campos()
 
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.text_experiencias.delete("1.0", tk.END)
        self.entry_linkedin.delete(0, tk.END)
        self.entry_status_emprego.delete(0, tk.END)
        self.entry_expectativa_salarial.delete(0, tk.END)
        self.curriculo_path.set("")
 
    def selecionar_curriculo(self):
        curriculo = filedialog.askopenfilename()
        self.curriculo_path.set(curriculo)
 
def main():
    app = tk.Tk()
    CandidatoApp(app)
    app.mainloop()
 
if __name__ == "__main__":
    main()