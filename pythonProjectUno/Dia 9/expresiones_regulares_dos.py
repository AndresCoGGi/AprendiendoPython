import re

texto = "llama al 435-525-6588 ya mismo"
patron = r'\d{3}-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto)
# con re.compiler puedo obtner cada grupito individual

print(resultado)
print(resultado.group())





#ejercicio dos
texto = "No atendemos los martes en la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar)

#ejercicio
clave = input("clave: ")
patron = r'\D{1}\w{7}'
chequear = re.search(patron,clave)
print(chequear)