import tkinter as tk

def open_candidato():
    candidato_app = tk.Tk()
    candidato_app.title("Cadastro de Desenvolvedor")

    # Aqui você pode incluir o código para a opção "Sou candidato"
    # que você forneceu

    candidato_app.mainloop()

def open_recrutador():
    recrutador_app = tk.Tk()
    recrutador_app.title("Visualizar Candidatos")

    # Aqui você pode incluir o código para a opção "Sou recrutador"
    # que você forneceu

    recrutador_app.mainloop()

# Tela inicial
app = tk.Tk()
app.title("Tela Inicial")

candidato_button = tk.Button(app, text="Sou candidato", command=open_candidato)
candidato_button.pack()

recrutador_button = tk.Button(app, text="Sou recrutador", command=open_recrutador)
recrutador_button.pack()

app.mainloop()

