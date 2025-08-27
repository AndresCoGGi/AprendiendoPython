class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print('Ja ja')

    def hablar(self):
        print("que tal")


#Herencia multiple
class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
#Madre y Padre tienen el metodo hablar, pero el prioriza el primer del que heredo, en este caso Padre
mi_nieto.hablar()
mi_nieto.reir()
#se puede ver el orden de las herencias
print(Nieto.__mro__)