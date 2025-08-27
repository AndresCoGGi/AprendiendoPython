def cualquier_nombre(palabra):
    lista = []
    for letra in palabra:
        if letra in lista:
            continue
        else:
            lista.append(letra)
    lista.sort()
    return lista

#otra forma : uso de sets pero luego transformarlo en una lista
print(cualquier_nombre("entretenido"))