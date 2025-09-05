import random
import pygame
import math
from pygame import mixer

# Inicializar a pygame
pygame.init()

# definir pantalla para el juego
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono(buscar en flaticon)
pygame.display.set_caption('Invasion Espacial Andru')
icono = pygame.image.load('ovni-military-transport.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# Agregar Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load('astronave.png')
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0

# enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('nave-extraterrestre.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 530
bala_y_cambio = 3
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

#texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    # que la bala salga de la mitad del jugador
    pantalla.blit(img_bala, (x + 16, y + 10))


# funcion para detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# loop del juego
se_ejecuta = True
while se_ejecuta:
    # rellenar pantalla en color RGB
    # pantalla.fill((25, 39, 156))
    # rellenar con pantalla de fondo
    pantalla.blit(fondo, (0, 0))

    # por cada evento que ocurra - iterar eventos
    for evento in pygame.event.get():
        # evento para cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # evento para presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.9
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.9
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        # evento para soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantener bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 530:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener bordes del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 530
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        # poner enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 530
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Poner jugador
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)
    # actualizar
    pygame.display.update()
