import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

#el codigo fuente de la pagina
#print(resultado.text)

#para permitir navegar en los elementos del HTML
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)

#devuelve una lista con el contenido de los elementos de title
print(sopa.select('title')[0].getText())

parrafo = sopa.select('div')[40].getText()
print(parrafo)

#extraer una clase
columna_lateral = sopa.select('.widget-content a')
for a in columna_lateral:
    print(a.getText())

#extraer imagenes
imagenes = sopa.select('img')[0]
print(imagenes['src'])

imagen = requests.get(imagenes['src'])
f = open('Mi imagen.jpg','wb')
f.write(imagen.content)
f.close()