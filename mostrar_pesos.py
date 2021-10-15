"""
Experimentacion, no es necesario.
"""
from persistencia_red_neuronal import cargar
from graficos import plot_SD
import statistics
def mostrar_pesos():
    red = cargar()
    print("tamaño red")
    print(len(red))
    for layer in red:
        print("PESOS W")
        print(layer.W)
        print("PESOS Bias")
        print(layer.B)

def prueba_plot_Desviacion():

    lista = [6,2,3,1]
    stdev = statistics.stdev(lista)

    plot_SD(lista, stdev)


prueba_plot_Desviacion()

