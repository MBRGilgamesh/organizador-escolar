import tkinter as tk
from agenda import abrir_agenda
from checklist import abrir_checklist
from dados import carregar_dados

# Criar janela principal
janela = tk.Tk()

# Título da janela
janela.title("Organizador Escolar")

# Tamanho da janela
janela.geometry("400x300")

# Título do aplicativo
titulo = tk.Label(
    janela,
    text="ORGANIZADOR ESCOLAR",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=20)

# Botão Agenda
botao_agenda = tk.Button(
    janela,
    text="Agenda Escolar",
    width=20,
    height=2,
    command=abrir_agenda
)

botao_agenda.pack(pady=10)

# Botão Checklist
botao_checklist = tk.Button(
    janela,
    text="Checklist de Estudos",
    width=20,
    height=2,
    command=abrir_checklist
)

botao_checklist.pack(pady=10)

# Botão sair
botao_sair = tk.Button(
    janela,
    text="Sair",
    width=15,
    command=janela.destroy
)

botao_sair.pack(pady=20)

carregar_dados()
# Manter programa aberto
janela.mainloop()