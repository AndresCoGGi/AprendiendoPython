from pathlib import Path
import os
#crear instancias de Path
base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(base)
print(guia)
#crear un objeto path nuevo
guia2 = guia.with_name("La_perrera.txt")
print(guia2)
#devuelve el antecesor inmediato, ir por el arbol genealogico de los objetvos encarpetados
print(guia.parent.parent)
guia_tres = Path(Path.home(),'Europa')
for txt in Path(guia_tres).glob("**/*.txt"):
    print(f"AQUUIIII {txt}")
#recuperar una porcion de una ruta
guia_cuatro = Path("Europa", "España", "Barcelona", "sagrada_familia.txt")
en_europa = guia_cuatro.relative_to(Path("Europa"))
en_espania = guia_cuatro.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)