import pandas as pd

resultados = "resultados/"

def guardarCSV(array, nombre):
    pd.DataFrame(array).to_csv(resultados+nombre+".csv")


def guardarPlano(valor, nombre):
    with open(resultados+nombre+".txt", "a") as text_file:
        text_file.write(str(valor)+"\n")
