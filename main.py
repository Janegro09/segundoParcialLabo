import pygame
import colores
import fn_aux
from enemigos import NaveVerde
from personaje import NavePpal
from constantes import *

pygame.init()
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GALAGA")

flag_run = True

# TIMER fabrique un evento independiente del usuario que se ejecuta una vez cada mls que le indique
timer = pygame.USEREVENT
pygame.time.set_timer(timer,100)
flag_limite = True
clock = pygame.time.Clock()
#Creamos personaje ppal
player = NavePpal(PATH_IMG+"ship.png",36, 36,ANCHO_VENTANA/2,ALTO_VENTANA - 80)

#CREAMOS ENEMIGOS
total_enemigos = range(7)
lista_enemigos_verde = []
lista_enemigos_azul = []
lista_enemigos_rojo = []

for i in total_enemigos:
    lista_enemigos_verde.append(NaveVerde(0+i*70,BASE_ENEMIGA ,TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA,10,PATH_IMG+"spiked1.PNG"))
    lista_enemigos_azul.append(NaveVerde(0+i*70,BASE_ENEMIGA + TAMANIO_NAVE_ENEMIGA + 10,TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA,10,PATH_IMG+"spiked2.PNG"))
    lista_enemigos_rojo.append(NaveVerde(0+i*70,BASE_ENEMIGA +(TAMANIO_NAVE_ENEMIGA + 10)*2,TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA,10,PATH_IMG+"spiked3.PNG"))

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",20)
texto = fuente.render("PUNTAJE:", True, colores.COLOR_AMARILLO_ARENA)

#Sentido de las naves
sentido1 = True
sentido2 = True
sentido3 = True

imagen_fondo = pygame.image.load(PATH_IMG+"fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

while flag_run:
    ventana_principal.blit(imagen_fondo,imagen_fondo.get_rect())
    # ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)
    delta_ms = clock.tick(FPS)
    
    #PLAYER UPDATE
    player.mover(ANCHO_VENTANA, ALTO_VENTANA)


    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if (evento.type == pygame.QUIT):
            flag_run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            rec_pos = evento.pos
        if evento.type == pygame.USEREVENT:
            sentido1 = fn_aux.mover_naves(lista_enemigos_verde, ANCHO_VENTANA, TAMANIO_NAVE_ENEMIGA,sentido1)
            sentido2 = fn_aux.mover_naves(lista_enemigos_azul, ANCHO_VENTANA, TAMANIO_NAVE_ENEMIGA,sentido2)
            sentido3 = fn_aux.mover_naves(lista_enemigos_rojo, ANCHO_VENTANA, TAMANIO_NAVE_ENEMIGA,sentido3)

    # PERSONAJE DRAW
    player.actualizar_pantalla(ventana_principal)

    # ENEMY DRAW
    for nave in lista_enemigos_verde:
        nave.actualizar_pantalla(ventana_principal)
    for nave in lista_enemigos_azul:
        nave.actualizar_pantalla(ventana_principal)
    for nave in lista_enemigos_rojo:
        nave.actualizar_pantalla(ventana_principal)

    pygame.display.flip()

pygame.quit()