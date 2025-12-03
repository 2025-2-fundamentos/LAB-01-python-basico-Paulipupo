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
        data.append((line[0], int(line[1])))
        
    return sorted(data)

def wordcount_reducer(mapped_data):
    result = []
    for key, value in mapped_data:
        if result and result[-1][0] == key:
            result[-1] = (key, max(result[-1][1], value), min(result[-1][2], value))
        else:
            result.append((key, value, value))
            
    return result

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    data = read_data("files/input/")
    mapped_data = wordcount_mapper(data)
    return wordcount_reducer(mapped_data)

print(pregunta_05())