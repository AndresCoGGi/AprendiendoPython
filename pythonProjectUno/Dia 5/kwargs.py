def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor
    return total

print(suma(x=3,y=5,z=2))

def describir_persona(nombre,**kwargs):
    print(f"Caracteristicas de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona("Maria", color_ojos = "azules", color_pelo = "rubio")