#ayudas. metodo choice
#funciones: pedir letras, validar letras, cequear letra, ver si gano
#sugerencias
from random import choice

lista = []


def elegir_palabra(lista_palabras):
    palabra = choice(lista_palabras)
    return palabra


def validar_letra(palabra, letra_nueva):
    letra_valida = False
    index = 0
    for letra in palabra:
        if letra == letra_nueva:
            lista[index] = letra_nueva
            letra_valida = True
        index += 1
    return letra_valida


def llenar_lista_vacia(palabra):
    for i in range(len(palabra)):
        lista.append("_")


def validar_ganar(palabra):
    palabra_actual = ""
    for i in lista:
        palabra_actual = palabra_actual + i
    if palabra_actual == palabra:
        return True
    else:
        return False


def main():
    lista_letras = []
    vidas = 6
    lista_palabras = ['santiago', 'andres', 'bere', 'elkin', 'laura', 'william']
    print("Bienvenido al juego del ahorcado")
    palabra = elegir_palabra(lista_palabras)
    llenar_lista_vacia(palabra)
    print("Adivina esta palabra")
    print(lista)
    while vidas != 0:
        letra = input("Ingrese una letra: ").lower()
        if letra not in lista_letras:
            lista_letras.append(letra)
        else:
            print("⚠️ Esta letra ya fue ingresada, por favor ingrese una nueva letra")
            continue  # vuelve al inicio del while
        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Por favor ingresa **una sola letra válida**.")
            continue  # vuelve al inicio del while
        if validar_letra(palabra, letra):
            print("Bien hecho")
            if validar_ganar(palabra):
                print("Felicitaciones ganaste")
                break
        else:
            vidas = vidas - 1
            if vidas == 0:
                print("Lo siento has perdido")
                print(f"la palabra era: {palabra}")
        print(lista)
        print(f"Te quedan {vidas} vidas")

main()






