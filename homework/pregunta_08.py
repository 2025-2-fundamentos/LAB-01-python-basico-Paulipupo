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
        data.append((int(line[1]), line[0]))
        
    return sorted(data)

def wordcount_reducer(mapped_data):
    result = []
    for key, value in mapped_data:
        if result and result[-1][0] == key:
            result[-1] = (key, result[-1][1] + [value])
        else:
            result.append((key, [value]))
            
    return [(k, sorted(set(v))) for k, v in result]

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    
    data = read_data("files/input/")
    letters = wordcount_mapper(data)
    return wordcount_reducer(letters)

    
