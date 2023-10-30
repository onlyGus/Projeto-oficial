import tkinter as tk

from tkinter import ttk

 

janela = tk.Tk()

 

def escolha_carreira ():

    print ("Back-end: %d\n Front-end: %d\n Full-stack: %d" %(var1.get(), var2.get(), var3.get()))

 

ttk.Label (janela, text="Escolha sua carreira:").grid(row=0, sticky=tk.W)

var1 = tk.IntVar ()

ttk.Checkbutton (janela, text= "Back-end", variable=var1).grid (row=1, sticky=tk.W)

 

var2 = tk.IntVar ()

ttk.Checkbutton (janela, text= "Front-end", variable=var2).grid (row=2, sticky=tk.W)

 

var3 = tk.IntVar ()

ttk.Checkbutton (janela, text= "Full-stack", variable=var3).grid (row=3, sticky=tk.W)

 

 

tk.Button (janela, text='Sair', command=janela.quit).grid (row=4, sticky=tk.W,pady=4)

tk.Button (janela, text='Mostrar', command=escolha_carreira).grid (row=5,sticky=tk.W,pady=4)

 

tk.mainloop()