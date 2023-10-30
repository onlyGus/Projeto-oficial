import tkinter as tk
import sqlite3

def visualizar_candidatos():
    conn = sqlite3.connect('dados_devs.db')
    cursor = conn.cursor()

    cidade = entry_cidade.get()
    estado = entry_estado.get()
    expectativa_salarial = entry_expectativa_salarial.get()

    # Construir a consulta com base nos campos preenchidos
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

    # Executar a consulta
    cursor.execute(query, values)
    candidatos = cursor.fetchall()

    # Atualizar a lista na interface
    text_candidatos.delete("1.0", tk.END)
    if candidatos:
        for candidato in candidatos:
            text_candidatos.insert(tk.END, f"{candidato}\n")
    else:
        text_candidatos.insert(tk.END, "Nenhum candidato encontrado.")

    # Fechar conexão
    conn.close()

# Interface Gráfica para Recrutador
recrutador_app = tk.Tk()
recrutador_app.title("Visualizar Candidatos")

# Elementos da interface
tk.Label(recrutador_app, text="Cidade:").grid(row=0, column=0)
entry_cidade = tk.Entry(recrutador_app)
entry_cidade.grid(row=0, column=1)

tk.Label(recrutador_app, text="Estado:").grid(row=1, column=0)
entry_estado = tk.Entry(recrutador_app)
entry_estado.grid(row=1, column=1)

tk.Label(recrutador_app, text="Expectativa Salarial:").grid(row=2, column=0)
entry_expectativa_salarial = tk.Entry(recrutador_app)
entry_expectativa_salarial.grid(row=2, column=1)

text_candidatos = tk.Text(recrutador_app, height=10, width=50)
text_candidatos.grid(row=4, column=0, columnspan=2)

tk.Button(recrutador_app, text="Visualizar Candidatos", command=visualizar_candidatos).grid(row=5, column=0, columnspan=2)

recrutador_app.mainloop()