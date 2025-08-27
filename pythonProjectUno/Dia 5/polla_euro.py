from random import *
import time

participantes = ["Elkin", "Jorge", "Santi", "William", "Daniel", "Andres"]
marcadores = ["España 0-0 Inglaterra",
              "España 0-1 Inglaterra",
              "España 0-2 Inglaterra",
              "España 0-3 Inglaterra",
              "España 0-4 Inglaterra",
              "España 1-0 Inglaterra",
              "España 2-0 Inglaterra",
              "España 3-0 Inglaterra",
              "España 4-0 Inglaterra",
              "España 1-1 Inglaterra",
              "España 1-2 Inglaterra",
              "España 1-3 Inglaterra",
              "España 1-4 Inglaterra",
              "España 2-1 Inglaterra",
              "España 3-1 Inglaterra",
              "España 4-1 Inglaterra",
              "España 2-2 Inglaterra",
              "España 2-3 Inglaterra",
              "España 2-4 Inglaterra",
              "España 3-2 Inglaterra",
              "España 4-2 Inglaterra",
              "España 3-3 Inglaterra",
              "España 3-4 Inglaterra",
              "España 4-3 Inglaterra",
              ]

index = 23
print("Bienvenido a la polla Europea")
print("Generando Marcadores.......")
print()
time.sleep(5)
for persona in participantes:

    aleatorio_uno = randint(0, index)
    marcador_uno = marcadores[aleatorio_uno]
    marcadores.pop(aleatorio_uno)
    index = index - 1

    aleatorio_dos = randint(0, index)
    marcador_dos = marcadores[aleatorio_dos]
    marcadores.pop(aleatorio_dos)
    index = index - 1

    aleatorio_tres = randint(0, index)
    marcador_tres = marcadores[aleatorio_tres]
    marcadores.pop(aleatorio_tres)
    index = index - 1

    aleatorio_cuatro = randint(0, index)
    marcador_cuatro = marcadores[aleatorio_cuatro]
    marcadores.pop(aleatorio_cuatro)
    index = index - 1

    print(f"{persona} le corresponden los siguientes marcadores: ")
    print(marcador_uno)
    print(marcador_dos)
    print(marcador_tres)
    print(marcador_cuatro)
    print()