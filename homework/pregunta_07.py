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
    numbers = set()
    
    for line in or_data:
        data.append((int(line[1]), line[0]))
        numbers.add(int(line[1]))
        
    return data, sorted(numbers)

def wordcount_reducer(mapped_data, numbers):
    result = [(number, []) for number in numbers ]
    
    for key, value in mapped_data:
        index = numbers.index(key)
        result[index][1].append(value)
    return result

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    data = read_data("files/input/")
    letters, numbers = wordcount_mapper(data)
    return wordcount_reducer(letters, numbers)