import numpy as np

class neural_layer():
    """
    Esta clase sirve como una estructura de dato, aqui se guardan los pesos
    bias y la funcion de activacion que se utiliza en una capa.

    Los pesos y los bias se inicializan con valores aleatorios entre 0 y 1.
    """
    def __init__(self, numero_conexiones_que_llegan, numero_neuronas,funcion_activacion):
        self.funcion_activacion= funcion_activacion
        #es un vector, con valores entre 0 y 1
        self.B= np.random.rand(1,numero_neuronas)*2-1
        #matriz de numero_conexion*numero_neuronas con valores entre 0 y 1
        self.W= np.random.rand(numero_conexiones_que_llegan,numero_neuronas)*2-1


def crear_red_neuronal(topologia, act_f):
    """Dado un array con el numero de nodos en cada capa (topologia) y su funcion de activacioon, devuelve
    un Array de capas."""
    red_neuronal = []
    #recorremos el array hasta el ultimo valor, no inclusive.
    for indice, layer in enumerate(topologia[:-1]):
        #agregamos capa con cantidad de conexiones, neuronas, y funcion activacion, a la red.
        red_neuronal.append(neural_layer(topologia[indice], topologia[indice+1], act_f))
    return red_neuronal