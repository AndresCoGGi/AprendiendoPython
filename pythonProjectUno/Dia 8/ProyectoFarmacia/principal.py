from os import system
import numeros


def main():
    querer_turno = True

    system('clear')
    while querer_turno:
        opcion = input("Bienvenido, a que area desea ir: \n"
                       "[1] - Perfumeria\n"
                       "[2] - Farmacia\n"
                       "[3] - Cosmeticos\n")
        try:
            opcion = int(opcion)
        except ValueError:
            system('clear')
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue
        if opcion not in range(1, 4):
            system('clear')
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue
        system('clear')
        numeros.decorar_generador(opcion)
        seguir = input("Quieres otro turno: \n"
                       "[1] - Si\n"
                       "[2] - No\n")
        try:
            seguir = int(seguir)
        except ValueError:
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue
        if seguir not in range(1, 3):
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue
        if seguir == 2:
            querer_turno = False
        system('clear')


main()
