import random

import pygame

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
img_enemigo = pygame.image.load('nave-extraterrestre.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

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
        #evento para presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                coordenada_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                coordenada_x_cambio = 0.3
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
    enemigo_x += enemigo_x_cambio

    # mantener bordes del enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    #Poner jugador y enemigo
    jugador(coordenada_x, coordenada_y)
    enemigo(enemigo_x, enemigo_y)
    #actualizar
    pygame.display.update()