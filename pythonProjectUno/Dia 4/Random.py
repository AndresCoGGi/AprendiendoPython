#importar todas los metodos de libreria de Random
from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio_dos = uniform(1,10)
print(round(aleatorio_dos,1))

#numero aleatorio entre 0 y 1
aleatorio_tres = random()
print(aleatorio_tres)

colores = ['azul','rojo','verde','amarillo']
aleatorio_cuatro = choice(colores)
print(aleatorio_cuatro)

#mezclar
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)



