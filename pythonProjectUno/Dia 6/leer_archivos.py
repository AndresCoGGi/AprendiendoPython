#segundo parametro de la funcion open es el modo
#r o vacio -- solo lectura
#w - solo escritura
#a - solo escritura y se posiciona el cursor al final

mi_archivo = open('prueba.txt')



#print(mi_archivo.read()) #leer all archive
#print(mi_archivo.readline()) #lee una linea
#print(mi_archivo.readlines()) #almacena lineas en listas

#for l in mi_archivo:
 #   print("Aqui dice : "+l)





mi_archivo.close()
