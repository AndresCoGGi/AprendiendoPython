#conversion implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2
#python hizo la conversion automaticamente de num1 a tipo float
print(type(num1))
print(type(num2))

#conversion explicita
numero1 = 5.8
print(numero1)
print(type(numero1))

#convertir de float a int
numero2 = int(numero1)
print(numero2)
print(type(numero2))

edad = input("Dime tu edad: ")
print("tu edad es "+edad)

nueva_edad = 1 + int(edad)
print("vas a cumplir "+str(nueva_edad))