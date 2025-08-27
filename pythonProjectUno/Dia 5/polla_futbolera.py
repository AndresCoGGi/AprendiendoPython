from random import *
import time

participantes = ["Elkin", "Jorge", "Santi", "William", "Daniel", "Andres"]
marcadores = ["Colombia 0-0 Argentina",
              "Colombia 0-1 Argentina",
              "Colombia 0-2 Argentina",
              "Colombia 0-3 Argentina",
              "Colombia 0-4 Argentina",
              "Colombia 1-0 Argentina",
              "Colombia 2-0 Argentina",
              "Colombia 3-0 Argentina",
              "Colombia 4-0 Argentina",
              "Colombia 1-1 Argentina",
              "Colombia 1-2 Argentina",
              "Colombia 1-3 Argentina",
              "Colombia 1-4 Argentina",
              "Colombia 2-1 Argentina",
              "Colombia 3-1 Argentina",
              "Colombia 4-1 Argentina",
              "Colombia 2-2 Argentina",
              "Colombia 2-3 Argentina",
              "Colombia 2-4 Argentina",
              "Colombia 3-2 Argentina",
              "Colombia 4-2 Argentina",
              "Colombia 3-3 Argentina",
              "Colombia 3-4 Argentina",
              "Colombia 4-3 Argentina",
              ]

index = 23
print("Bienvenido a la polla copa america")
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