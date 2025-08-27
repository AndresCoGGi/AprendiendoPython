def contar_primos(numero):
    contador = 0
    for i in range(2, numero+1):
        if es_primo(i):
            contador += 1
    return contador


def es_primo(numero):
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(f"El número de primos entre 0 y 100 es: {contar_primos(100)}")
print(f"El número de primos entre 0 y 7 es: {contar_primos(7)}")
print(f"El número de primos entre 0 y 50 es: {contar_primos(50)}")
print(f"El número de primos entre 0 y 150 es: {contar_primos(150)}")
print(f"El número de primos entre 0 y 1 es: {contar_primos(1)}")