texto = "Este es el texto de Andres"
print(texto.upper())
print(texto.lower())
print(texto.split("t"))
#find a diferencia de index, es que no lanza un error sino un -1
print(texto.find("s"))
print(texto.replace("Andres","Andresito"))
print(texto.replace("e","x"))

a="aprender"
b="python"
c = "genial"

e = " ".join([a,b,c])
print(e)