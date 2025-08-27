class Pajaro:

    alas = True

    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #metodos de instancia
    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"volar {metros} metros")

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    #metodos de clase
    #los metodos de clase no necesitan una instancia para poder ejecutarse
    # se puede cambiar los atributos de la clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False


    #metodos estaticos
    #no se relacionan con las instancia y no se cambian los atributos de las instancias
    @staticmethod
    def mirar():
        print("El pajaro mira")



piolin = Pajaro("amarillo","canario")
piolin.alas = False

Pajaro.poner_huevos(3)
Pajaro.mirar()