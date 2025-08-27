#JUEGO - ADIVINA NUMERO
from random import randint

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre} he pensado un numero entre el 1 y el 100, cual crees que es ? Tienes 8 intentos")

#En cada intento el jugador dira 1 numero y el programa podra responder de 4 formas
#1. si el numero es menor a 1 o superior a 100 - numero no permitido
#2. si el numero es menor al numero a adivinar, le dira respuesta incorrecta, y que el # ingresado es menor
#3. si el numero es mayor al numero a adivinar, le dira respuesta incorrecta, y que el # ingresado es mayor
#4. si acerto, dice que gano y en cuantos intetno gano

intentos = 8
numero_aleatorio = randint(1, 100)
while intentos > 0:
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado < 1 or numero_ingresado > 100:
        print("Numero no permitido")
        intentos = intentos - 1
        if intentos == 0:
            print("PERDISTE NO TE QUEDAN MAS INTENTOS")
            print(f"El # a adivinar era {numero_aleatorio}")
        else:
            print(f"Te quedan {intentos} intentos")
    elif numero_ingresado < numero_aleatorio:
        print("Respuesta incorrecta, numero esperado es mayor")
        intentos = intentos - 1
        if intentos == 0:
            print("PERDISTE NO TE QUEDAN MAS INTENTOS")
            print(f"El # a adivinar era {numero_aleatorio}")
        else:
            print(f"Te quedan {intentos} intentos")
    elif numero_ingresado > numero_aleatorio:
        print("Respuesta incorrecta, numero esperado es menor")
        intentos = intentos - 1
        if intentos == 0:
            print("PERDISTE NO TE QUEDAN MAS INTENTOS")
            print(f"El # a adivinar era {numero_aleatorio}")
        else:
            print(f"Te quedan {intentos} intentos")
    else:
        intentos = intentos - 1
        print(f"FELICITACIIONES {nombre} GANASTE, LO LOGRASTE EN {8 - intentos} INTENTOS")
        print(f"El # a adivinar era {numero_aleatorio}")
        intentos = 0
