def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))

print("Hola mundo")

print(next(g))
# el generador siempre se va a acordar donde va su ejecucion

