#segundo parametro de la funcion open es el modo
#r o vacio -- solo lectura
#w - solo escritura y se reemplazo por lo que hay
#a - solo escritura y se posiciona el cursor al final

archivo = open('prueba_dos.txt', 'a')
archivo.write('\nhola Mundo')
archivo.close()

archivo_dos = open('pruebatres.txt', 'w')
lista = ['hola','mundo','aqui','estoy']
for p in lista:
    archivo_dos.writelines(p + '\n')
archivo_dos.close()