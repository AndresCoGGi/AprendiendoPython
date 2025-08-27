#diccionario : clave y valor
diccionario = {"c1":"valor 1", "c2":"valor2"}
print(diccionario)
print(type(diccionario))
resultado = diccionario["c1"]
print(resultado)


cliente = {'Nombre':'Juan',
           'Apellido':'Fuentes',
           'Peso':88,
           'talla':1.70}
consulta = cliente['Apellido']
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s1'])

dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())

diccionarioDos = {"c1":"valor 1", "c2":"valor2"}
#agregacion de elementos
diccionarioDos['c3'] = "valor3"
#modificacion
diccionarioDos['c2'] = "valor2Modi"
print(diccionarioDos)
#conocer todas las claves
print(diccionarioDos.keys())
#conocer valores
print(diccionarioDos.values())
#conocer
print(diccionarioDos.items())