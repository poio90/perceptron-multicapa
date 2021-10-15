# configurar red neuronal o cargar la red neuronal previa
import os
import sys

from sklearn.metrics import mean_squared_error

import entrenamiento as en
import graficos
import guardarExcel
from cargar_datos import cargar_datos
from config import read_config
from estructura import crear_red_neuronal
from funcion_activacion import sigm
from funcion_costo import error_cuadratico_medio as ecm
from persistencia_red_neuronal import *
import hashlib

# Disable print
#sys.stdout = open(os.devnull, 'w')


def porcentaje_aciertos(prediccion, respuesta)->str:
    acierto = 0
    for index, i in enumerate(prediccion):
        if (i>=0.5 and respuesta[index]>0.5) or (i<0.5 and respuesta[index]<0.5):
            acierto+=1

    porcentaje = 100*(acierto/len(prediccion))
    porcentaje = "{:.2f}".format(porcentaje)
    return porcentaje+"%"


# Esto deberia o estar dentro un objeto, o algo, para cargarlo como archivo de configuracion

con = read_config()

if con.usar_red_neuronal_guardada:
    # cargar red_neuronal
    red_neuronal = cargar()

else:
    red_neuronal = crear_red_neuronal(topologia=con.topologia, act_f=sigm)

if con.entrenar:
    # cargar datos
    data, respuesta = cargar_datos(con.path_datos)

    arrayMSE = []

    last_error = 0

    # ito -> intervalo de actualizacion del lr
    ito = con.intervalo_evaluacion_eta

    lr = con.tasa_aprendizaje
    arrayETA = [lr]

    # guardar primera red
    guardar(red_neuronal)

    # entrenamiento
    for i in range(con.epocas):
        prediccion = en.entrenar(red_neuronal=red_neuronal, Entrada=data, Respuesta=respuesta,
                                 funcion_costo=ecm, tasa_aprendizaje=lr, entrenar=True)
        MSE = mean_squared_error(respuesta, prediccion)
        arrayMSE.append(MSE)


        if last_error == 0:
            last_error = MSE
            print("")
            print("Tasa vieja " + str(lr))

        if ito == i:
            print("")
            print("error " + str(MSE))
            print("last_error " + str(last_error))
            print("Diferencia: " + str(MSE - last_error))
            old_lr = lr
            lr = en.eta_adaptativo(tasa_aprendizaje=lr,
                                   error=MSE, last_error=last_error, a=con.a, b=con.b)
            arrayETA.append(lr)
            last_error = MSE
            ito = ito + con.intervalo_evaluacion_eta
            print("")
            print("Tasa nueva " + str(lr))

            if lr > old_lr:
                # si es mayor la nueva tasa, significa que esta aprendiendo bien, guardamos copia
                guardar(red_neuronal)
            else:
                # caso contrario esta aprendiendo mal, volvemos a la red anterior.
                red_neuronal = cargar()

    graficos.plot_MSE(con.epocas, arrayMSE, nombre="MSE"+str(con))
    graficos.plot_ETA(arrayETA, nombre="ETA"+str(con), intervalo=con.intervalo_evaluacion_eta)
    guardarExcel.guardarPlano((MSE, str(con)), "MSE")
    # guardar red_neuronal
    guardar(red_neuronal=red_neuronal)


else:
    # cargar datos
    data, respuesta = cargar_datos(con.path_datos_evaluacion)

    # predecir
    prediccion = en.entrenar(red_neuronal=red_neuronal, Entrada=data, Respuesta=respuesta,
                             funcion_costo=ecm, tasa_aprendizaje=con.tasa_aprendizaje, entrenar=False)

    # mostrar performance de la red
    #valor = hashlib.md5(prediccion)
    #print(prediccion)
    MSE = mean_squared_error(respuesta, prediccion)
    porcentaje = porcentaje_aciertos(prediccion, respuesta)

    guardarExcel.guardarPlano((MSE, str(con), porcentaje), "MSE_evaluacion")
