#configurar red neuronal o cargar la red neuronal previa
from funcion_activacion import sigm
from estructura import crear_red_neuronal
from cargar_datos import cargar_datos
from persistencia_red_neuronal import *
import entrenamiento as en
from funcion_costo import error_cuadratico_medio as ecm
from config import read_config
#Esto deberia o estar dentro un objeto, o algo, para cargarlo como archivo de configuracion

con = read_config()



if con.usar_red_neuronal_guardada:
    # cargar red_neuronal
    red_neuronal = cargar()

else:
    red_neuronal = crear_red_neuronal(topologia=con.topologia, act_f=sigm)



if con.entrenar:
    # cargar datos
    data, respuesta = cargar_datos(con.path_datos)


    #entrenamiento
    for i in range(con.epocas):
        prediccion = en.entrenar(red_neuronal=red_neuronal, Entrada=data, Respuesta=respuesta,
                          funcion_costo=ecm, tasa_aprendizaje=con.tasa_aprendizaje, entrenar=True)


    # guardar red_neuronal
    guardar(red_neuronal=red_neuronal)



else:
    # cargar datos
    data, respuesta = cargar_datos(con.path_datos_evaluacion)

    #predecir
    prediccion = en.entrenar(red_neuronal=red_neuronal, Entrada=data, Respuesta=respuesta,
                          funcion_costo=ecm, tasa_aprendizaje=con.tasa_aprendizaje, entrenar=False)

    #mostrar performance de la red
