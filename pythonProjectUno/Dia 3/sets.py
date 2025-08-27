#los sets solo admiten elementos unicos, es decir no se repiten los valores que hay adentro
#si agregas un elemento repetido python lo descarta sin avisarte
#no estan indesados, no se conuslta por el indice
#los elementos son inmutables, y no se puyeden agregan ni listas ni diccionarios, si se pueden agregar tuples

#forma 1
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

#forma 2
otro_set = {8,9,10,11,11,1,2}
print(type(otro_set))
print(otro_set)

print(len(otro_set))
print(2 in otro_set)
#union de sets
set_nuevo = mi_set.union(otro_set)
print(set_nuevo)

#agregar a un set
set_nuevo.add(12)
set_nuevo.remove(11)
#discard igual al remove pero cuando voy a eliminar un elemento que no esta, no saca error
set_nuevo.discard(25)
#se puede usar el metodo pop - pero este elimina cualquier element
set_nuevo.pop()
# .clear - vaciar set
print(set_nuevo)
