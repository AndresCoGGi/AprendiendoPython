import os
import shutil

print(os.getcwd())
archivo = open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

# eliminar un archivo
#os.unlink('/Users/andrescogi/PycharmProjects/pythonProjectUno/Dia 8', )

# mover un archivo a otra ubicacion
#shutil.move('curso.txt','/Users/andrescogi/PycharmProjects/pythonProjectUno/Dia 8')

# eliminar una carpeta vacia
# os.rmdir

# eliminar una carpeta llena
# shutil.rmtree
# se puede instalar un modulo que envie a la papelera send2trash


# walk recorrer archivos
print(os.walk('/Users/andrescogi/Documents/'))
ruta = '/Users/andrescogi/Documents'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')


