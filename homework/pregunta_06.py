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
        entries = line[4].split(",")
        for entry in entries:
            key, value = entry.split(":")
            data.append((key, int(value)))
        
    return sorted(data)

def wordcount_reducer(mapped_data):
    result = []
    for key, value in mapped_data:
        if result and result[-1][0] == key:
            result[-1] = (key, min(result[-1][1], value), max(result[-1][2], value))
        else:
            result.append((key, value, value))
            
    return result

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    
    data = read_data("files/input/")
    mapped_data = wordcount_mapper(data)
    return wordcount_reducer(mapped_data)

