def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")

try:
    #Codigo que se quiere probar
    suma()
except:
    #en el except se puede poner el tipo de exception
    #except TypeError:
    #codigo a ejecutar si hay un error
    print("Algo no ha salido bien")
else:
    #codigo adicional a ejecutar si no hay error, es opcional
    print("Hiciste todo bien")
finally:
    #Codigo que se va a ejecutar de todos modos, es opcional
    print("Eso fue todo")


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")


pedir_numero()
