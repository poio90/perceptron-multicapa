"""
Experimentacion, no es necesario.
"""
from persistencia_red_neuronal import cargar


red = cargar()
print("tamaño red")
print(len(red))
for layer in red:
    print("PESOS W")
    print(layer.W)
    print("PESOS Bias")
    print(layer.B)