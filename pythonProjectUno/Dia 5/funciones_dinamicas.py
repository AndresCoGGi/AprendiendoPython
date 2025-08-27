def chequear_tres_cifras(numero):
    return numero in range(100, 1000)


resultado = chequear_tres_cifras(658)
print(resultado)


def chequear_3_cifras_list(lista):
    for numero in lista:
        if numero in range(100, 1000):
            return True
        else:
            pass
    return False


resultado = chequear_3_cifras_list([2,453,65,1])
print(resultado)


def chequear_numero_tres_cifras(lista):
    lista_tres_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            lista_tres_cifras.append(numero)
        else:
            pass
    return lista_tres_cifras


resultado = chequear_numero_tres_cifras([1,54,123,1,467])
print(resultado)