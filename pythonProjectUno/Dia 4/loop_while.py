
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1



monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else:
    print("No tengo mas monedas")

respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir? s/n: ")
else:
    print("Gracias")

#usar pass
#respuestaDos = "s"
#while respuestaDos == "s":
 #   pass

#print("Hola Mundo")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)



