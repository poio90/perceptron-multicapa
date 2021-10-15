# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import time


def plot_ETA(y: list, nombre:str, intervalo:int):
    plt.clf()
    x = [intervalo*i for i in range(len(y))]
    plt.plot(x, y)
    plt.xlabel('x - epocas')
    plt.ylabel('y - tasa de aprendizaje')
    last_eta = "{:.4f}".format(y[-1])
    plt.title('ultimo eta: '+last_eta)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    plt.savefig(f'resultados/{nombre} date={timestr}.png')


def plot_MSE(epoca:int, y:list, nombre:str):
    x = np.arange(1, (epoca+1))
    plt.plot(x, y)
    # naming the x axis
    plt.xlabel('x - epocas')
    # naming the y axis
    plt.ylabel('y - error cuadratico medio')

    # giving a title to my graph
    plt.title('Error cuadratico medio')

    # function to show the plot
    #plt.show()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    plt.savefig(f'resultados/{nombre} date={timestr}.png')

