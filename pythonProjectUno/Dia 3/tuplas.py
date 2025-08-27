#la tuplas son similares a los diccionarios pero son inmutables, una vez un valor
#esta asignado a una clave no se puede modificar
#ocupan menos espacio de memorias, se procesan mas rapido
#almancenar esctrucutras que no queremos que sean modificadas
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
print(mi_tuple[0])
otro_taple = (1,2,(0,2),4)
print(otro_taple[2][0])
#convertir taple en lista y viceversa
mi_tuple = list(mi_tuple)
mi_tuple = tuple(mi_tuple)
#asignar contenido del tuble a variables
tt = (1,2,3)
x,y,z = tt
print(x,y,z)

yy = (1,2,3,1)
print(len(yy))
#contar cantidad de apariciones de un valor
print(yy.count(1))
#consulta indice
print(yy.index(2))

