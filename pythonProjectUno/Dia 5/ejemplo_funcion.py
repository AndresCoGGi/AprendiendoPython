precios_cafe = [('capuchino',2.5),('Expreso',1.2),('Moca',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    caffe_mas_caro = ''
    for cafe,precio  in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            caffe_mas_caro = cafe
    return (caffe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(cafe,precio)