import tkinter as tk
from candidato import CandidatoApp
from recrutador import RecrutadorApp


class IndexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela Inicial")
        self.master.geometry("400x400")
 
        candidato_button = tk.Button(self.master, text="Sou candidato", command=self.open_candidato)
        candidato_button.pack()
 
        recrutador_button = tk.Button(self.master, text="Sou recrutador", command=self.open_recrutador)
        recrutador_button.pack()
 
    def open_candidato(self):
        candidato_app = tk.Tk()
        CandidatoApp(candidato_app)
 
    def open_recrutador(self):
        recrutador_app = tk.Tk()
        RecrutadorApp(recrutador_app)
 
def main():
    app = tk.Tk()
    IndexApp(app)
    app.mainloop()
 
if __name__ == "__main__":
    main()