from pathlib import Path
import os
import shutil
from os import system


def obtener_numero_recetas():
    contador = 0
    guia = Path(Path.home(), 'Recetas')
    for txt in Path(guia).glob("**/*.txt"):
        contador += 1
    return contador


def obtener_categorias_actuales():
    lista_categorias = []
    categorias = Path(Path.home(), 'Recetas')
    for subcarpeta in categorias.iterdir():
        if subcarpeta.is_dir():
            elemento = os.path.basename(subcarpeta)
            lista_categorias.append(elemento.lower())
    return lista_categorias


def obtener_recetas_actuales(categoria):
    lista_recetas = []
    subcarpeta = Path(Path.home(), 'Recetas', categoria)
    print("Tienes estas recetas: ")
    for archivo in subcarpeta.glob("*.txt"):
        print(f"  {Path(os.path.basename(archivo)).stem}".replace("_", " "))
        lista_recetas.append(Path(os.path.basename(archivo)).stem)
    return lista_recetas


def leer_recetas():
    lista_categorias = obtener_categorias_actuales()
    categoria = input(f"Seleccione una categoria {lista_categorias} : ").lower()
    if categoria not in lista_categorias:
        print("⚠️ la categoria es invalida")
        leer_recetas()
    else:
        lista_recetas = obtener_recetas_actuales(categoria)
        receta = input("Por favor escriba la receta que quiere leer: ").replace(" ", "_").lower()
        if receta not in lista_recetas:
            print("⚠️ Esta receta no existe, verifique e intente de nuevo")
        else:
            receta = receta + '.txt'
            receta_seleccionada = Path(Path.home(), 'Recetas', categoria, receta)
            print("*****AQUI TIENES LAS INSTRUCCIONES DE TU RECETA SELECCIONADA******")
            print(receta_seleccionada.read_text())
            print("********FIN DE LA RECETA**********")


def crear_receta():
    lista_categorias = obtener_categorias_actuales()
    categoria = input(f"Seleccione una categoria {lista_categorias} : ").lower()
    if categoria not in lista_categorias:
        print("⚠️ la categoria es invalida")
        crear_receta()
    else:
        nombre = input("Por favor ingrese el nombre de la receta que desea crear: ").replace(" ", "_").lower()
        if nombre in obtener_recetas_actuales(categoria):
            print("⚠️ Esta receta ya existe")
        else:
            nombre = nombre + '.txt'
            ruta = Path(Path.home(), 'Recetas', categoria, nombre)
            contenido = input("Ingrese su receta: ")
            ruta.write_text(contenido)


def crear_categoria():
    lista_categorias = obtener_categorias_actuales()
    categoria = input("Ingrese el nombre de la categoria que desea crear: ").lower()
    if categoria in lista_categorias:
        print("⚠️ Esta categoria ya existe")
        crear_categoria()
    else:
        os.makedirs('/Users/andrescogi/Recetas/'+categoria+'')
        print("Categoria creada con exito")


def eliminar_receta():
    lista_categorias = obtener_categorias_actuales()
    categoria = input(f"Seleccione una categoria {lista_categorias} : ").lower()
    if categoria not in lista_categorias:
        print("⚠️ la categoria es invalida")
        eliminar_receta()
    else:
        lista_recetas = obtener_recetas_actuales(categoria)
        receta = input("Por favor escriba la receta que quiere eliminar: ").replace(" ", "_").lower()
        if receta not in lista_recetas:
            print("⚠️ Esta receta no existe, verifique e intente de nuevo")
        else:
            receta = receta + '.txt'
            receta_seleccionada = Path(Path.home(), 'Recetas', categoria, receta)
            receta_seleccionada.unlink()
            print("Receta eliminada")


def eliminar_categoria():
    lista_categorias = obtener_categorias_actuales()
    categoria = input("Ingrese el nombre de la categoria que desea eliminar: ")
    eliminar = categoria
    if categoria.lower() in lista_categorias:
        ruta = Path('/Users/andrescogi/Recetas') / eliminar
        shutil.rmtree(ruta)
        #os.rmdir('/Users/andrescogi/Recetas/' + eliminar + '')
        print("Categoria eliminada con exito")
    else:
        print("⚠️ Esta categoria no existe")
        eliminar_categoria()


def enrutador(opcion):
    match opcion:
        case 1:
            leer_recetas()
        case 2:
            crear_receta()
        case 3:
            crear_categoria()
        case 4:
            eliminar_receta()
        case 5:
            eliminar_categoria()
    volver = input("Ingrese una letra para volver al menu principal: ")


def main():
    opcion = ''
    print("Hola bienvenido al administrador de recetas")
    print(f"las recetas estan en: {Path(Path.home(), 'Recetas')}")
    while opcion != 6:
        print(f"Tienes {obtener_numero_recetas()} recetas")
        opcion = input("Elija una opcion 1-6: \n"
                       "[1] - Leer receta\n"
                       "[2] - Crear receta\n"
                       "[3] - Crear categoria\n"
                       "[4] - Eliminar receta\n"
                       "[5] - Eliminar categoria\n"
                       "[6] - Finalizar programa\n")
        try:
            opcion = int(opcion)
        except ValueError:
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue
        if opcion not in range(1, 7):
            print("⚠️ Esta opcion no es valida, por favor ingresar una opcion valida")
            continue  # vuelve al inicio del while
        if opcion != 6:
            enrutador(opcion)
        system('clear')


main()
