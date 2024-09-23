"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    """
    Construye un dataframe de Pandas a partir del archivo 'clusters_report.txt'.
    
    Los nombres de las columnas están en minúsculas, reemplazando los espacios por guiones bajos.
    Las palabras clave están separadas por coma y con un solo espacio entre palabra y palabra.
    """

    with open('clusters_report.txt', 'r') as text_file:
        lineas = text_file.readlines()[4:]  # Saltar las primeras 4 líneas


    # Definir función para formatear títulos
    def title_format(header):
        return header.lower().replace(" ", "_")


    # Inicializar lista para almacenar datos
    data = {
        "cluster": [],
        "cantidad_de_palabras_clave": [],
        "porcentaje_de_palabras_clave": [],
        "principales_palabras_clave": []
    }


    cluster = [0, 0, 0, '']
    for linea in lineas:
        # Verificar si la línea comienza con un número
        if re.match('^ +[0-9]+ +', linea):
            number, quantity, percentage, *words = linea.split()
            cluster[0] = int(number)
            cluster[1] = int(quantity)
            cluster[2] = float(percentage.replace(',', '.').replace('%', ''))
            
            # Unir palabras clave
            words = ' '.join(words)
            cluster[3] = words
            
        # Verificar si la línea comienza con una letra minúscula
        elif re.match('^ +[a-z]', linea):
            words = linea.split()
            words = ' '.join(words)
            cluster[3] += ' ' + words
            
        # Verificar si la línea está vacía
        elif re.match('^\n', linea) or re.match('^ +$', linea):
            # Agregar datos a la lista
            data["cluster"].append(cluster[0])
            data["cantidad_de_palabras_clave"].append(cluster[1])
            data["porcentaje_de_palabras_clave"].append(cluster[2])
            data["principales_palabras_clave"].append(cluster[3].strip())
            
            # Reinicializar cluster
            cluster = [0, 0, 0, '']


    # Construir dataframe
    df = pd.DataFrame(data)
    return df


print(ingest_data())
