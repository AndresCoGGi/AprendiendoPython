nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese valor de ventas: ")
comision = round(float(ventas)*0.13,2)
print(f"Hola {nombre} tu comision es de ${comision}")