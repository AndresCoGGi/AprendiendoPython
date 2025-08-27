#dos objetos de formas distintas pueden ejecutar un metodo con el mismo nombre
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')


#aqui esta la magia, en cada iteracion el ejecuta el metodo de cada objeto
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)