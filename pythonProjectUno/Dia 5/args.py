#no sabemos cuantos argumentos se van a recibir en la funcion, se usa *args, se adaptan al numero
#de argumentos, es decir que la funcion reciba argumentos variables

#*args es una convencion pero se puede usar cualquier palabra
def suma(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

print(suma(5,6,3))
print(suma(5,6,))