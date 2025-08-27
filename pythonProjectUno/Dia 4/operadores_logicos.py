#operadores de comparacion ==, >=, <=, !=, >,<
#operadores logicos "y","o","No": AND, OR, NOT
min_bool = (4 < 5) and (5 < 6) #se deben cumplir las 2 condiciones
print(min_bool)

otro_bool = (55==55) and ('perro' == 'perro')
print(otro_bool)

bool_tres = 1==10 or 3==3 #como minimos se debe cumplir una
print(bool_tres)

texto = "esta frase es breve"
validacion = "frase" in texto
print(validacion)

validacionDos = ("frase" in texto) and ("breve" in texto)
print(validacionDos)

bool_cuatro = not ("a" == "a") #negacion
print(bool_cuatro)
