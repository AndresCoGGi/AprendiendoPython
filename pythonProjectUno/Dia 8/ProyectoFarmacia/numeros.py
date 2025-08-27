def generador_perfumeria():
    p = 0
    while True:
        yield "P-0" + str(p)
        p += 1


def generador_farmacia():
    f = 0
    while True:
        yield "F-0" + str(f)
        f += 1


def generador_cosmeticos():
    c = 0
    while True:
        yield "C-0" + str(c)
        c += 1


gp = generador_perfumeria()
gf = generador_farmacia()
gc = generador_cosmeticos()


def decorar_generador(opcion):
    print("Su turno es: ")
    if opcion == 1:
        print(next(gp))
    elif opcion == 2:
        print(next(gf))
    else:
        print(next(gc))
    print("Aguarde, en un momento sera atendido")
