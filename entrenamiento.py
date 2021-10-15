import numpy as np

def entrenar(red_neuronal, Entrada, Respuesta, funcion_costo, tasa_aprendizaje=0.05, entrenar=True):
    """Si entrenar esta en true, se obtiene los resultados del forward_pass, luego se hace el proceso de backpropagation
    donde se calculan los deltas, y luego con esto se realiza el aprendizaje por el desenso de gradiente"""
    #Forward pass, meter la entrada, y guardar la respuesta predicha.
    out = forward_pass(red_neuronal=red_neuronal, Entrada=Entrada)
    if entrenar:
        #backward pass
        deltas = []
        #se comienza a recorrer desde la ultima capa
        for indice in reversed(range(0, len(red_neuronal))):
            z = out[indice+1][0]
            a = out[indice+1][1]
            
            if indice == len(red_neuronal)-1:
                #calcular deltas ultima capa
                deltas.insert(0, funcion_costo[1](a, Respuesta)*red_neuronal[indice].funcion_activacion[1](a))
            else:
                #calcular deltas respecto de capa previa
                deltas.insert(0, deltas[0]@ _W.T *red_neuronal[indice].funcion_activacion[1](a))
            
            _W = red_neuronal[indice].W

            #ajustar pesos y bias por el metodo del gradient descent
            red_neuronal[indice].B = red_neuronal[indice].B - np.mean(deltas[0], axis=0, keepdims=True) * tasa_aprendizaje
            red_neuronal[indice].W = red_neuronal[indice].W - out[indice][1].T @ deltas[0] * tasa_aprendizaje
    
    return out[-1][1]




def forward_pass(red_neuronal, Entrada):
    out = [(None, Entrada)]
    for indice, layer in enumerate(red_neuronal):
        #Multiplicacion matricial de el vector entrada por el vector de pesos de la primera capa, y se le suma los bias de la primera capa
        z = out[-1][1] @ red_neuronal[indice].W + red_neuronal[indice].B

        #salida de la funcion de activacion
        a = red_neuronal[indice].funcion_activacion[0](z)
        #guardamos para despues hacer backpropagation
        out.append((z,a))
    return out


