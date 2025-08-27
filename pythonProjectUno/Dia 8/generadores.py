def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


#en lugar de el return se usa el yield, para no almacenar en memroia el resultado
def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

#de esta forma pido a mi generador que me de el resultado de la funcion, si dvuelve varios, se va iterando
g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
