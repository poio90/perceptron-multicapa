import numpy as np

error_cuadratico_medio = (lambda Ypredicha, Yreal: np.mean((Ypredicha-Yreal)**2),
                          lambda Yp, Yr: (Yp-Yr))
"""Es una tupla, el primer valor tiene la funcion el segundo su derivada.
funcion= Error cuadratico medio
funcion -> error_cuadratico_medio[0]()  derivada -> error_cuadratico_medio[1]()"""
