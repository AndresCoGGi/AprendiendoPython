##tiene guiones al principio o al final
class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    #forma en que quiero que se sumistre un string de mi clase
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    #metodo de mi objeto que devuelve el largo de mi CD
    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD")


mi_cd = CD('Pink Floyd', 'The wall', 24)
print(str(mi_cd))
print(len(mi_cd))

#funcion eliminar
del mi_cd
