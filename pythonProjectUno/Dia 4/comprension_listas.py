#forma 1
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

#forma mas eficiente
palabra_dos = "HolaMundo"
lista = [letra for letra in palabra_dos]
print(lista)

#la primera n le puedo hacer operaciones matematicas
#si hay else debe ir despues de la primera n
lista_numeros = [n for n in range(0,21,2) if n * 2 > 10]
print(lista_numeros)

pies = [10,20,30,40,50]
metros = [pie*3.281 for pie in pies]
print(metros)
