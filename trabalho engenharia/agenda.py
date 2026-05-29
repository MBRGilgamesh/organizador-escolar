import tkinter as tk
from tkinter import messagebox
from dados import (
    eventos,
    tarefas,
    salvar_dados
)


def adicionar_evento():

    disciplina = entrada_disciplina.get()
    data = entrada_data.get()
    descricao = entrada_descricao.get()

    # Verifica campo vazio
    if (
        disciplina == ""
        or data == ""
        or descricao == ""
    ):

        messagebox.showwarning(
            "Erro",
            "Preencha todos os campos"
        )

        return

    evento = (
        f"{disciplina} - "
        f"{descricao} - "
        f"{data}"
    )

    eventos.append(evento)
    
    tarefas.append(

        "[ ] Estudar "

        + disciplina

        + " - "

        + descricao

        )

    salvar_dados()

    atualizar_lista()

    entrada_disciplina.delete(0, tk.END)
    entrada_data.delete(0, tk.END)
    entrada_descricao.delete(0, tk.END)


def remover_evento():

    selecionado = lista_eventos.curselection()

    if not selecionado:

        messagebox.showwarning(
            "Erro",
            "Selecione um evento"
        )

        return

    indice = selecionado[0]

    eventos.pop(indice)

    salvar_dados()

    atualizar_lista()


def atualizar_lista():

    lista_eventos.delete(
        0,
        tk.END
    )

    for evento in eventos:

        lista_eventos.insert(
            tk.END,
            evento
        )


def abrir_agenda():

    global entrada_disciplina
    global entrada_data
    global entrada_descricao
    global lista_eventos

    janela_agenda = tk.Toplevel()

    janela_agenda.title(
        "Agenda Escolar"
    )

    janela_agenda.geometry(
        "500x450"
    )

    titulo = tk.Label(

        janela_agenda,

        text="AGENDA ESCOLAR",

        font=(
            "Arial",
            16,
            "bold"
        )

    )

    titulo.pack(
        pady=10
    )

    tk.Label(

        janela_agenda,

        text="Disciplina:"

    ).pack()

    entrada_disciplina = tk.Entry(

        janela_agenda,

        width=30

    )

    entrada_disciplina.pack()

    tk.Label(

        janela_agenda,

        text="Data:"

    ).pack()

    entrada_data = tk.Entry(

        janela_agenda,

        width=30

    )

    entrada_data.pack()

    tk.Label(

        janela_agenda,

        text="Descrição:"

    ).pack()

    entrada_descricao = tk.Entry(

        janela_agenda,

        width=30

    )

    entrada_descricao.pack()

    tk.Button(

        janela_agenda,

        text="Adicionar Evento",

        command=adicionar_evento

    ).pack(
        pady=5
    )

    tk.Button(

        janela_agenda,

        text="Excluir Evento",

        command=remover_evento

    ).pack(
        pady=5
    )

    lista_eventos = tk.Listbox(

        janela_agenda,

        width=50,

        height=10

    )

    lista_eventos.pack(
        pady=10
    )

    atualizar_lista()

    tk.Button(

        janela_agenda,

        text="Voltar",

        command=janela_agenda.destroy

    ).pack()