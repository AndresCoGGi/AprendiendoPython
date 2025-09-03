import random
import pygame
import math

#Inicializar a pygame
pygame.init()

#definir pantalla para el juego
pantalla = pygame.display.set_mode((800, 600))

#titulo e icono(buscar en flaticon)
pygame.display.set_caption('Invasion Espacial Andru')
icono = pygame.image.load('ovni-military-transport.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')


#Jugador
img_jugador = pygame.image.load('astronave.png')
coordenada_x = 368
coordenada_y = 530
coordenada_x_cambio = 0

#enemigo
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

#variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 530
bala_y_cambio = 3
bala_visible = False

#puntaje
puntaje = 0


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    #que la bala salga de la mitad del jugador
    pantalla.blit(img_bala, (x + 16, y + 10))

# funcion para detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


#loop del juego
se_ejecuta = True
while se_ejecuta:
    # rellenar pantalla en color RGB
    #pantalla.fill((25, 39, 156))
    # rellenar con pantalla de fondo
    pantalla.blit(fondo, (0, 0))

    #por cada evento que ocurra - iterar eventos
    for evento in pygame.event.get():
        #evento para cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento para presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                coordenada_x_cambio = -0.6
            if evento.key == pygame.K_RIGHT:
                coordenada_x_cambio = 0.6
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = coordenada_x
                    disparar_bala(bala_x, bala_y)
        #evento para soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                coordenada_x_cambio = 0

    #modificar ubicacion del jugador
    coordenada_x += coordenada_x_cambio

    # mantener bordes
    if coordenada_x <= 0:
        coordenada_x = 0
    elif coordenada_x >= 736:
        coordenada_x = 736

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):
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
            bala_y = 530
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        #poner enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 530
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    #Poner jugador
    jugador(coordenada_x, coordenada_y)

    #actualizar
    pygame.display.update()