"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import glob


def read_data(input_folder):
    data = []
    files = glob.glob(f"{input_folder}*")
    
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                data.append(line.strip().split("\t"))
            
    return data
                    
def wordcount_mapper(or_data):
    data = []
    for line in or_data:
        data.append((line[0], len(line[3].split(",")), len(line[4].split(","))))
        
    return data


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data = read_data("files/input/")
    return wordcount_mapper(data)