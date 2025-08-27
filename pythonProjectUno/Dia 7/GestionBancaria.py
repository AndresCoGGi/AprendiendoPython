# Gestion Bancaria
# Crear clase persona con atributos: nombre y apellido
# Crear clase cliente que hereda de persona, nro cuenta y balance
    # metodos: imprimir cliente, con todos los datos
    # metodo: depositar, cuando dinero agregar
    # metodo: retirar, cuando dinero retirar
#codigo principal
  # que el usuario elija si quiere hacer depositos o retiros o salir
  # el codigo debe llevar cuenta de cuanto es el balance del cliente
        # y que no pueda retirar mas de lo que posee
        # funciones
            # crear cliente y devolver un cliente creado como objeto
            # inicio -- organizar la ejecucion, crear cliente y mantener la ejecucion en lo loop
            # no se realizaran validaciones de las entradas del cliente. el cliente siempre ingresara info bien

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        # herencia del constructor del padre
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Informacion del cliente: \n Nombre: {self.nombre} \n Apellido: {self.apellido} "
                f"\n Numero Cuenta: {self.numero_cuenta} \n Balance: {self.balance}")

    def depositar(self):
        deposito = input("Por favor ingrese cuando desea depositar en su cuenta: ")
        self.balance += int(deposito)
        print("Deposito Aceptado")

    def retirar(self):
        retiro = input("Por favor ingrese el monto que desea retirar: ")
        if int(retiro) > self.balance:
            print(f"Fondos insuficiente, tu salgo actual es: {self.balance}")
        else:
            self.balance -= int(retiro)


#Codigo Principal
import random


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = random.randint(100, 1000)
    balance = 0
    cliente = Cliente(nombre,apellido,numero_cuenta, balance)
    return cliente


def main():
    opcion = 0
    cliente = crear_cliente()
    print("*****Bienvenido al Banco de Belalcazar*****")
    while opcion != 4:
        print(f"Hola {cliente.nombre} ")
        opcion = input("Elija una opcion 1-3: \n"
                       "[1] - Ver cuenta\n"
                       "[2] - Depositar\n"
                       "[3] - Retirar\n"
                       "[4] - Salir\n")
        opcion = int(opcion)
        if opcion == 1:
            print("Esta es la informacion de tu cuenta: ")
            print(str(cliente))
        elif opcion == 2:
            cliente.depositar()
        elif opcion == 3:
            cliente.retirar()


main()
