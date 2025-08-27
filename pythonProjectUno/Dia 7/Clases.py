class Pajaro:

    alas = True

    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #metodos de clase
    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"volar {metros} metros")


mi_pajaro = Pajaro('negro','Tucan')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)
print(mi_pajaro.alas)

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(230)
