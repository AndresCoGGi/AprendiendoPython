def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return saber_mayor(num1,num2,num3)
    elif suma < 10:
        return saber_menor(num1,num2,num3)
    else:
        return saber_intermedio(num1,num2,num3)

#opcion 2
def devolver_distintos_dos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

def saber_mayor(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

def saber_menor(num1, num2, num3):
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    else:
        return num3

def saber_intermedio(num1, num2, num3):
    if num1>num2 and num1<num3:
        return num1
    elif num2>num1 and num2<num3:
        return num2
    else:
        return num3

print(devolver_distintos(2,3,4))
print(devolver_distintos(4,10,3))
print(devolver_distintos(5,2,4))

print(devolver_distintos_dos(2,3,4))
print(devolver_distintos_dos(4,10,3))
print(devolver_distintos_dos(5,2,4))

