#Caracteres especiales
#Estos se usan para identificar tipos de caracteres en una cadena:

#\d → Dígito numérico (0-9)
#\w → Carácter alfanumérico (letras y números, incluyendo _)
#\s → Espacio en blanco (espacios, tabulaciones, saltos de línea)
#\D → No numérico
#\W → No alfanumérico
#\S → No espacio en blanco
##Cuantificadores
#Indican cuántas veces debe aparecer un carácter o grupo:

#+ → Una o más veces
#* → Cero o más veces
#? → Cero o una vez
#{n} → Exactamente n veces
#{n,} → n veces o más
#{n,m} → Entre n y m veces




import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda) #busqueda tiene diferentes metodos

busquedaDos = re.findall(patron, texto)
print(busquedaDos)

def verificar_email(email):
    patron = r'\w+@\w+\.com\W?\w*'
    if re.match(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

def verificar_saludo(frase):
    patron = r'^Hola'
    if re.match(patron,frase):
        print("Ok")
    else:
        print("No has saludado")


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    if re.match(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
