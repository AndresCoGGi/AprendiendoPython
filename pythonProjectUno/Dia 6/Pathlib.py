from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/andrescogi/Alternativo/otro_archivo.txt')
#no es necesario poner el open
if not carpeta.exists():
    print('este archivo no existe')
else:
    print('Genial, existe')
    print(carpeta.read_text())
    print(carpeta.name)
    print(carpeta.suffix)
    print(carpeta.stem)

#convierte en ruta windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

