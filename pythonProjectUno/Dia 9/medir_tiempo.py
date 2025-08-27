import timeit

#calcula el tiempo de ejecucion
declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 10000000)
print(duracion)

declaracion_dos = '''
prueba_while(10)
'''

mi_setup_dos = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion_dos = timeit.timeit(declaracion_dos, mi_setup_dos, number = 10000000)
print(duracion_dos)