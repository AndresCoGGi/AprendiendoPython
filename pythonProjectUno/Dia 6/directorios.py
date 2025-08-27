import os
ruta = os.getcwd() #obtener ruta actual
ruta_dos = os.chdir('/Users/andrescogi/Alternativo') #obtener ruta de un archivo
ruta_tres = os.makedirs('/Users/andrescogi/Alternativo/otra') #crear carpeta o archivo
ruta_cinco = os.rmdir('/Users/andrescogi/Alternativo/otra') #eleminar directorio
archivo = open('otro_archivo.txt')
print(ruta_dos)
print(archivo.read())

ruta_cuatro = '/Users/andrescogi/Alternativo/otro_archivo.txt'
elemento = os.path.basename(ruta_cuatro)
print(elemento)
elemento_dos = os.path.dirname(ruta_cuatro)
print(elemento_dos)
elemento_tres = os.path.split(ruta_cuatro) #devolver en una tupla base y nombre archivo
print(elemento_tres)

#forma tradicional
otro_archivo = open('/Users/andrescogi/Alternativo/otro_archivo.txt')
print(otro_archivo.read())
