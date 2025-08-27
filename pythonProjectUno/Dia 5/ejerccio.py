lista_numeros = [1,2,2,3,1,3]
def reducir_lista(lista):
    nueva_lista = list(set(lista)) #quita duplicados
    nueva_lista.reverse() #invierte el orden
    return nueva_lista

print(reducir_lista(lista_numeros))