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


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    
    data = read_data("files/input/")
    suma_total = 0
    for row in data:
        suma_total += int(row[1])
        
    return suma_total
