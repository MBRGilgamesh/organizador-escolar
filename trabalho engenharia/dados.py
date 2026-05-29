import json


eventos = []

tarefas = []


def salvar_dados():

    dados = {

        "eventos": eventos,

        "tarefas": tarefas

    }

    with open(

        "dados.json",

        "w",

        encoding="utf-8"

    ) as arquivo:

        json.dump(

            dados,

            arquivo,

            ensure_ascii=False,

            indent=4

        )


def carregar_dados():

    global eventos
    global tarefas

    try:

        with open(

            "dados.json",

            "r",

            encoding="utf-8"

        ) as arquivo:

            dados = json.load(
                arquivo
            )

            eventos.clear()
            tarefas.clear()

            eventos.extend(
                dados.get(
                    "eventos",
                    []
                )
            )

            tarefas.extend(
                dados.get(
                    "tarefas",
                    []
                )
            )

    except:

        pass