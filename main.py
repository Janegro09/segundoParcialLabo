import pygame
import colores
import random
from helpers import *
from enemigos import Enemigos
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
player = NavePpal(ANCHO_VENTANA/2,ALTO_VENTANA-100)

#CREAMOS ENEMIGOS
total_filas = range(3)
total_columnas = range(8)

lista_enemigos = []

for i in total_columnas:
    for j in total_filas:
        tipo = random.randint(1,3)
        tipo_nave = mandale_nave(tipo)
        # self,posx,posy,puntaje,parametro
        lista_enemigos.append(Enemigos(i*TAMANIO_NAVE_ENEMIGA,j*TAMANIO_NAVE_ENEMIGA,10,1,tipo_nave))

total_enemigos = range(7)

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",20)
texto = fuente.render("PUNTAJE:", True, colores.COLOR_AMARILLO_ARENA)

imagen_fondo = pygame.image.load(PATH_IMG+"fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#Sonido del juego
pygame.mixer.music.load("music/stage1.mp3")
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)

#Sentido de las naves enemigas
sentido = "DER"

while flag_run:
    ventana_principal.blit(imagen_fondo,imagen_fondo.get_rect())
    # ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)
    delta_ms = clock.tick(FPS)
    
    #PLAYER UPDATE
    player.control("STAY")

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if (evento.type == pygame.QUIT):
            flag_run = False

        if evento.type == pygame.KEYDOWN:
            if(evento.key == pygame.K_SPACE):
                player.control("SHOT")

        if evento.type == pygame.USEREVENT:
            sentido = mover_naves(lista_enemigos, sentido)

    # PERSONAJE DRAW&UPDATE
    player.update(delta_ms)
    player.draw(ventana_principal)
    # SHOT DRAW
    for misil in player.disparos:
        misil.actualizar_pantalla(ventana_principal,player.velocidad)

    # ENEMY DRAW&UPDATE
    total_enemigos_vivos = contar_enemigos_vivos(lista_enemigos)
    potenciador = 1 if total_enemigos_vivos==0 else int(len(lista_enemigos)/total_enemigos_vivos)
    for nave in lista_enemigos:
        nave.update(delta_ms,potenciador,player.disparos)
        nave.draw(ventana_principal)
        for misil in nave.disparos:
            if not player.inmune:
                if misil.rectangulo.colliderect(player.rectangulo):
                    player.control("DEAD")
                    misil.mostrar = False
            misil.actualizar_pantalla(ventana_principal,nave.velocidad_disparo,"enemigo")
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()