import tkinter as tk
import candidato
import recrutador

def open_candidato():
    candidato_app = tk.Toplevel()
    candidato_app.title("Cadastro de Desenvolvedor")
    candidato.create_candidato_page(candidato_app)

def open_recrutador():
    recrutador_app = tk.Toplevel()
    recrutador_app.title("Visualizar Candidatos")
    recrutador.create_recrutador_page(recrutador_app)

# Tela inicial
app = tk.Tk()
app.title("Tela Inicial")

candidato_button = tk.Button(app, text="Sou candidato", command=open_candidato)
candidato_button.pack()

recrutador_button = tk.Button(app, text="Sou recrutador", command=open_recrutador)
recrutador_button.pack()

app.mainloop()
