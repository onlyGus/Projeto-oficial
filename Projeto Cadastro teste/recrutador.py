import tkinter as tk
import sqlite3
 
class RecrutadorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizar Candidatos")
 
        tk.Label(self.master, text="Cidade:").grid(row=0, column=0)
        self.entry_cidade = tk.Entry(self.master)
        self.entry_cidade.grid(row=0, column=1)
 
        tk.Label(self.master, text="Estado:").grid(row=1, column=0)
        self.entry_estado = tk.Entry(self.master)
        self.entry_estado.grid(row=1, column=1)
 
        tk.Label(self.master, text="Expectativa Salarial:").grid(row=2, column=0)
        self.entry_expectativa_salarial = tk.Entry(self.master)
        self.entry_expectativa_salarial.grid(row=2, column=1)
 
        self.text_candidatos = tk.Text(self.master, height=10, width=50)
        self.text_candidatos.grid(row=4, column=0, columnspan=2)
 
        tk.Button(self.master, text="Visualizar Candidatos", command=self.visualizar_candidatos).grid(row=5, column=0, columnspan=2)
 
    def visualizar_candidatos(self):
        conn = sqlite3.connect('dados_devs.db')
        cursor = conn.cursor()
 
        cidade = self.entry_cidade.get()
        estado = self.entry_estado.get()
        expectativa_salarial = self.entry_expectativa_salarial.get()
 
        query = "SELECT * FROM desenvolvedores"
 
        conditions = []
        values = []
 
        if cidade:
            conditions.append("cidade = ?")
            values.append(cidade)
        if estado:
            conditions.append("estado = ?")
            values.append(estado)
        if expectativa_salarial:
            conditions.append("expectativa_salarial = ?")
            values.append(expectativa_salarial)
 
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
 
        cursor.execute(query, values)
        candidatos = cursor.fetchall()

        self.text_candidatos.delete("1.0", tk.END)
        if candidatos:
            for candidato in candidatos:
                self.text_candidatos.insert(tk.END, f"{candidato}\n")
        else:
            self.text_candidatos.insert(tk.END, "Nenhum candidato encontrado.")
 
        conn.close()
 
def main():
    app = tk.Tk()
    RecrutadorApp(app)
    app.mainloop()
 
if __name__ == "__main__":
    main()