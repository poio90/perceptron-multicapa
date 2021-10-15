import pandas as pd
import numpy as np

def cargar_datos(path:str):
    """
    dado el path, retorna una tupla con= un numpy.narray primer array filas, segundo array valores de las columnas
    con= numpy.narray donde solo tiene valores de la ultima columna del dataset.
    """
    data_set_diabetes = pd.read_csv(path)

    data = data_set_diabetes.to_numpy()
    #numpy.ndarray

    respuestas = data[:, -1]
    respuestas = respuestas[:, np.newaxis]
    data = data[:, :-1]

    # Prueba de que anda normalizar
    # prueba = np.array([[23,0.1,1000],[54,0.7,2000],[42,0.4,1444]])
    # print("shape prueba"+str(prueba.shape))
    # normalizar(prueba)
    # print(prueba)

    normalizar(data)

    return data, respuestas



def normalizar(data):
    """Dado los datos normalizara las columnas con la ecuacion (x-min)/(max-min)
    prueba = np.array([[23,0.1,1000],[54,0.7,2000]])
    para prueba[0][0]=23 -> (23-23)/(54-23)
    para prueba[0][1]=0.1 -> (0.1-0.1)/(0.7-0.1)
    """
    for i in range(len(data[0])):
        minimo, maximo = buscar_min_max_a_traves_de_columnas(data, i)
        for instancia in data:
            instancia[i] = (instancia[i] - minimo)/(maximo - minimo)




def buscar_min_max_a_traves_de_columnas(array_de_arrays, posicion):
    """Dado un array de array, reccorrera la posicion x de cada uno buscando el minimo."""
    minimo = array_de_arrays[0][posicion]
    maximo = minimo
    for array in array_de_arrays:
        value = array[posicion]
        if value < minimo:
            minimo = value
        elif value > maximo:
            maximo = value

    return minimo, maximo

