#analizador de texto
#pedir a un usuario un texto
#pedir al usuario 3 letras
#analisis
#1.cuantas veces aparecen las letras - usar listas y metodos de string, pasar a minuscula
#2.cuantas palabras hay en esa frase - metodos String
#3.primera y ultima palabra del texto - usar indexacion
#4.mostrar el texto con orden de las palabras al reves. revertir en una lista y unir con espacios
#5.decir si aparece o no la palabra python. usar booleanos y diccionarios para asociar el booleano aun String
texto = input("Por favor ingrese un texto: ").lower()
letraUno = input("Ingresar la primera letra: ").lower()
letraDos = input("Ingrese la segunda letra: ").lower()
letraTres = input("Ingrese la tercera letra: ").lower()
palabrasTexto = texto.split()
cantidadPalabras = len(palabrasTexto);
print("******ANALISIS DE TEXTO**********")
print(f"la letra {letraUno} aparece {texto.count(letraUno)} veces en el texto")
print(f"la letra {letraDos} aparece {texto.count(letraDos)} veces en el texto")
print(f"la letra {letraTres} aparece {texto.count(letraTres)} veces en el texto")
print(f"En este texto hay {cantidadPalabras} palabras")
print("la primera palabra del texto es "+palabrasTexto[0])
print("la ultima palabra del texto es "+palabrasTexto[cantidadPalabras-1])
palabrasTexto.reverse()
textoReves = " ".join(palabrasTexto)
print("El texto al reves es: "+textoReves)
estaPython = "python" in palabrasTexto
diccionario = {True:"Si",False:"No"}
print(f"la palabra 'python' {diccionario[estaPython]} esta en el texto")





