serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

cliente = {'nombre':'Federico',
           'edad':45,
           'ocupacion':'instructor'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'keanu reeves',
                              'director':'lana y lilly Wachows'}}

elementos = [cliente,pelicula,'libro']
for elemento in elementos:
    match elemento:
        case {'nombre':nombre,
           'edad':edad,
           'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre)
            print(edad)
            print(ocupacion)
        case {'titulo': titulo,
            'ficha_tecnica': {'protagonista': protagonista,
                              'director':director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
