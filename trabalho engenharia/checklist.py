import tkinter as tk
from tkinter import messagebox
from dados import (
    tarefas,
    salvar_dados
)

def adicionar_tarefa_automatica(texto):

    tarefas.append(
        "[ ] " + texto
    )

    try:

        atualizar_lista()

    except:

        pass

def adicionar_tarefa():

    tarefa = entrada_tarefa.get()

    if tarefa == "":

        messagebox.showwarning(
            "Erro",
            "Digite uma tarefa"
        )

        return

    tarefas.append(
        "[ ] " + tarefa
    )

    salvar_dados()

    atualizar_lista()

    entrada_tarefa.delete(
        0,
        tk.END
    )


def concluir_tarefa():

    selecionado = lista_tarefas.curselection()

    if not selecionado:

        messagebox.showwarning(
            "Erro",
            "Selecione uma tarefa"
        )

        return

    indice = selecionado[0]

    texto = tarefas[indice]

    if texto.startswith("[ ]"):

        tarefas[indice] = texto.replace(
            "[ ]",
            "[X]",
            1
        )

    salvar_dados()

    atualizar_lista()


def remover_tarefa():

    selecionado = lista_tarefas.curselection()

    if not selecionado:

        messagebox.showwarning(
            "Erro",
            "Selecione uma tarefa"
        )

        return

    indice = selecionado[0]

    tarefas.pop(indice)

    salvar_dados()

    atualizar_lista()


def atualizar_lista():

    lista_tarefas.delete(
        0,
        tk.END
    )

    for tarefa in tarefas:

        lista_tarefas.insert(
            tk.END,
            tarefa
        )


def abrir_checklist():

    global entrada_tarefa
    global lista_tarefas

    janela_checklist = tk.Toplevel()

    janela_checklist.title(
        "Checklist de Estudos"
    )

    janela_checklist.geometry(
        "500x450"
    )

    titulo = tk.Label(

        janela_checklist,

        text="CHECKLIST DE ESTUDOS",

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

        janela_checklist,

        text="Tarefa:"

    ).pack()

    entrada_tarefa = tk.Entry(

        janela_checklist,

        width=35

    )

    entrada_tarefa.pack()

    tk.Button(

        janela_checklist,

        text="Adicionar Tarefa",

        command=adicionar_tarefa

    ).pack(
        pady=5
    )

    tk.Button(

        janela_checklist,

        text="Concluir Tarefa",

        command=concluir_tarefa

    ).pack(
        pady=5
    )

    tk.Button(

        janela_checklist,

        text="Excluir Tarefa",

        command=remover_tarefa

    ).pack(
        pady=5
    )

    lista_tarefas = tk.Listbox(

        janela_checklist,

        width=45,

        height=10

    )

    lista_tarefas.pack(
        pady=10
    )

    atualizar_lista()

    tk.Button(

        janela_checklist,

        text="Voltar",

        command=janela_checklist.destroy

    ).pack()