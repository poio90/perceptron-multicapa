import dill as pickle

def guardar(red_neuronal):
    """Dada la red neuronal (un array de neural_layer) guarda todo (incluso las funciones de activacion)"""
    with open('red_neuronal.pkl', 'wb') as output:
        pickle.dump(red_neuronal, output, pickle.HIGHEST_PROTOCOL)

def cargar():
    """Carga la ultima red neuronal usada, si no hay ninguna error
    :return
     list() de estructura.neural_layer
    """
    with open('red_neuronal.pkl', 'rb') as input:
        red = pickle.load(input)
        return red

