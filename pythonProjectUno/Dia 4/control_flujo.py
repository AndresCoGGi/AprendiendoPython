#if - si
#elif - sino si
#else -sino
if 10 > 9:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "conejo"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No se que animal tienes")


edad = 17
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion > 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Eres adulto")
