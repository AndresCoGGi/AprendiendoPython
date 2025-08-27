#objetivo: que no importe en que sistema operativo estan los archivos
from Pathlib import Path
#asi seria la ruta en windows
carpeta = Path('\\Users\\andrescogi\\Alternativo') / 'otro_archivo.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())
