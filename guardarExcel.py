import os
import pandas as pd

resultados = "resultados/"

try:
    os.mkdir(resultados)
except OSError as e:
    pass

def guardarCSV(array, nombre):
    pd.DataFrame(array).to_csv(resultados+nombre+".csv")


def guardarPlano(valor, nombre):
    with open(resultados+nombre+".txt", "a") as text_file:
        text_file.write(str(valor)+"\n")
