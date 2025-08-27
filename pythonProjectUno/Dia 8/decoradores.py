# ejercicio previo
def cambiar_letra(tipo):
    def mayuscula_ej(texto):
        print(texto.upper())

    def minuscula_ej(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula_ej
    elif tipo == "min":
        return minuscula_ej


operacion = cambiar_letra("may")
operacion('palabra')

# Decoradores
print("Decoradores: ")


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion


@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


minuscula("Andru")
