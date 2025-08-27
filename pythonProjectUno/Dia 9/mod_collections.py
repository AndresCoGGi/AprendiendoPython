from collections import Counter, defaultdict, namedtuple
# Counter sirve para contar elementos repetidos
numeros = [8,6,4,5,7,3,4,2,4,2,6,3,8,6,4]

print(Counter(numeros))
print(Counter('missisipi'))
frase = 'al pan pan y al vino vino'
print((Counter(frase.split())))
serie = Counter(numeros)
# puede recibir el numero que quiero buscar serie.most_common(4)
print(serie.most_common())

# defaultdict crear un nuevo valor en base a una busqueda para no arrojar error, sino crear el elemento
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

# namedtuple, accese a tuplas a travez del nombre
Persona = namedtuple('Persona', ['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
print(ariel.peso)
print(ariel[2])