#lista, secuencia ordenada de datos de diferentes tipos
mi_lista = ["A","B","C"]
mi_lista_dos = ["D","E"]
otra_lista = ["hola",55,3.3]
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0])
#desde - hasta
print(mi_lista[0:2])
print(otra_lista[0])
print(mi_lista+mi_lista_dos)
#agregar elementos a una lisa
mi_lista_dos.append("F")
print(mi_lista_dos)
#eliminar elementos
mi_lista_dos.pop(2)
print(mi_lista_dos)
#ordenar listas
lista_alfabeto = ["g","o","m","a"]
lista_alfabeto.sort()
print(lista_alfabeto)
#invertir el orden
lista_alfabeto.reverse()
print(lista_alfabeto)