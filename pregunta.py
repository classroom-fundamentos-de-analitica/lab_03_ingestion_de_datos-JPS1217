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

    #
    # Inserte su código aquí
    #
    
    with open('clusters_report.txt', 'r') as text_file:
        df = text_file.readlines()
        df = df[4:]
       
    
    cls = []
    
    cluster = [0, 0, 0, '']
    for line in df:
        
        if re.match('^ +[0-9]+ +', line):
            number, quantity, percentage, *words = line.split()
            cluster[0] = int(number)
            cluster[1] = int(quantity)
            cluster[2] = float(percentage.replace(',', '.'))
            
            words.pop(0) #Eliminar el %
            words = ' '.join(words)
            cluster[3] += words
            
        elif re.match('^ +[a-z]', line):
            words = line.split()
            words = ' '.join(words)
            cluster[3] += ' ' + words
            
        elif re.match('^\n', line) or re.match('^ +$', line):
            cluster[3] = cluster[3].replace('.', '')
            cls.append(cluster)
            
            cluster = [0, 0, 0, '']
    
    return pd.DataFrame (cls, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])


print(ingest_data())
