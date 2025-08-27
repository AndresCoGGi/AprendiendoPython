lista = ['a','b','c']
for indice, item in enumerate(lista):
    print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1])
print(mis_tuples[1][0])