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
            key, _ = entry.split(":")
            data.append(key)
        
    return data

def wordcount_reducer(mapped_data):
    result = []
    for letter in set(mapped_data):
        result.append((letter, mapped_data.count(letter)))
        
    return sorted(result)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    data = read_data("files/input/")
    letters = wordcount_mapper(data)
    return dict(wordcount_reducer(letters))