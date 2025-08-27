nombres = ['Juan','Ana','Carlos','Belen','Fran', 'laura']
for nombre in nombres:
    numero_nombre = nombres.index(nombre) + 1
    print(f"Nombre {numero_nombre} es {nombre}")
    if nombre.startswith("l"):
        print("Nombre que empieza por l")
        print(nombre)
    else:
        print("Nombre que no empieza por l")
        print(nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

palabra = "python"
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,5]]:
    print(a)
    print(b)

dic = {"clave1":"a","clave2":"b","clave3":"c"}
for item in dic.values(): #solo valor
#for item in dic.items(): -- toda la info
#for item in dic: -- solo la clave
#for a,b in dic.items(): -- clave y valor
    print(item)
