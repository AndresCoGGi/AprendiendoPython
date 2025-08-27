def cero_repetido(*args):
    contador_ceros = 0
    for numero in args:
        if numero == 0 and contador_ceros != 2:
            contador_ceros = contador_ceros + 1
        elif contador_ceros == 1:
            contador_ceros = 0
        elif contador_ceros == 2:
            break
        else:
            continue
    if contador_ceros == 2:
        return True
    else:
        return False

print(cero_repetido(1, 2, 3, 4, 5))           # False
print(cero_repetido(0, 0, 1, 2, 3))           # True
print(cero_repetido(1, 2, 0, 0, 3, 4))        # True
print(cero_repetido(1, 2, 3, 4, 0, 0))        # True
print(cero_repetido(0, 1, 0, 2, 0))           # False
print(cero_repetido(1, 2, 0, 0, 0, 4))        # True
print(cero_repetido(5, 6, 0, 0, 3, 4))        # True
print(cero_repetido(1, 0, 0, 5, 0, 0))        # True
print(cero_repetido(0))                       # False
print(cero_repetido())                        # False