texto = "ABCDEFGHIJKLM"
#extraer caracteres desde 2 hasta 5
fragmento = texto[2:5]
print(fragmento)

textoDos = "ABCDEFGHIJKLM"
#extraer caracteres desde 2 hasta el final
fragmento = textoDos[2:]
print(fragmento)

textoTres = "ABCDEFGHIJKLM"
#extraer caracteres desde el inicio hasta el 5
fragmento = textoTres[:5]
print(fragmento)

textoCuatro = "ABCDEFGHIJKLM"
#extraer caracteres desde el 2 hasta el 10, de a 2
fragmento = textoCuatro[2:10:2]
print(fragmento)

textoCinco = "ABCDEFGHIJKLM"
#mostrar los caracteres invertidos
fragmento = textoCinco[::-1]
print(fragmento)