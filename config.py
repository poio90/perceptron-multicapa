from configparser import ConfigParser


def read_config():
    """

    :return: Pseudo diccionario, ojo
    """
    cf = ConfigParser()
    cf.read("config.ini")
    parametro = cf["PARAMETROS"]

    configuracion = CON(parametro)

    return configuracion


# objeto que tendra los atributos
class CON(object):

    def __str__(self):
        valor = f"top={self.diccionario['topologia']} " \
                f"epoch={self.diccionario['epocas']} " \
                f"ito={self.diccionario['intervalo_evaluacion_eta']}"
        return valor

    def __init__(self, diccionario):
        self.cantidad_de_entradas = int(diccionario["cantidad_de_entradas"])
        self.topologia = [int(s) for s in diccionario["topologia"].split(',')]
        self.topologia.insert(0, self.cantidad_de_entradas)
        self.tasa_aprendizaje = float(diccionario["tasa_aprendizaje"])
        self.entrenar = eval(diccionario["entrenar"])
        self.epocas = int(diccionario["epocas"])
        self.usar_red_neuronal_guardada = eval(diccionario["usar_red_neuronal_guardada"])
        self.path_datos = diccionario["path_datos"]
        self.path_datos_evaluacion = diccionario["path_datos_evaluacion"]
        self.intervalo_evaluacion_eta = int(diccionario["intervalo_evaluacion_eta"])
        self.a = float(diccionario["a"])
        self.b = float(diccionario["b"])
        self.diccionario = diccionario
