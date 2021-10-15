import numpy as np

sigm = (lambda x: 1/(1+np.e**(-x)),
        lambda x: x*(1-x))
"""Es una tupla, el primer valor tiene la funcion el segundo su derivada.
funcion= sigmoide 
funcion -> sigm[0]()  derivada -> sigm[1]()
"""


tanh = (lambda x: np.tanh(x),
        lambda x: 1 - (np.tanh(x)**2))
"""Es una tupla, el primer valor tiene la funcion el segundo su derivada.
funcion= tangente hiperbolica
funcion -> tanh[0]()  derivada -> tanh[1]()"""