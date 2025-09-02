import math
import os
import re
import datetime
import time

def generador_archivos():
    for carpeta, subcarpeta, archivo in os.walk('Mi_Gran_Directorio'):
        for arch in archivo:
            ruta = carpeta +"\\"+ arch
            leer = open(ruta)
            texto = leer.read()
            yield arch, texto
            leer.close()

def buscar_serie(texto):
    patron = r'N\D{3}-\d{5}'
    if re.search(patron, texto):
        return re.search(patron, texto).group(0)
    else:
        return None

def main():
    inicio = time.time()
    print(f'Fecha de búsqueda: {datetime.datetime.today().day}/{datetime.datetime.today().month}/{datetime.datetime.today().year}')
    print("ARCHIVO\t\t\t\tNRO. SERIE")
    print("-------\t\t\t\t----------")
    contador = 0
    for archivo, texto in generador_archivos():
        if buscar_serie(texto) is not None:
            contador += 1
            print(f'{archivo}"\t\t"{buscar_serie(texto)}')
    print(f'Números encontrados: {contador}')
    fin = time.time()
    print(f'Duración de la búsqueda: {math.ceil(fin - inicio)} segundos')

main()
