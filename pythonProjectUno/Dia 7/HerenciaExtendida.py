class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")\

    def hablar(self):
        print("Este animal emite un sonido")


#herencia, hereda de animal
class Pajaro(Animal):


    def __init__(self, edad, color, altura_vuelo):
        #herencia del constructor del padre
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


#la clase pajaro puede tener 3 tipos de metodos
#1. heredados de animal
#2. heredados modificados
#3. metodos nuevos en los hijos

#los pajaros puedes tener atributos propios

piolin = Pajaro(2, 'amarillo', 60)
mi_animal = Animal(2, 'rojo')


piolin.nacer()
piolin.hablar()
piolin.volar(100)

