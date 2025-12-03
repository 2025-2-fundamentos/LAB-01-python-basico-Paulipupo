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
    data = {}
    for line in or_data:
        key = line[0]
        if key not in data:
            data[key] = 0
            
        entries = line[4].split(",")
        for entry in entries:
            _, value = entry.split(":")
            data[key] += int(value)
            
            
    sorted_data = dict(sorted(data.items()))     
    return sorted_data


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
    data = read_data("files/input/")
    return wordcount_mapper(data)