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
total_filas = range(1)
total_columnas = range(10)

lista_enemigos = []

for i in total_columnas:
    for j in total_filas:
        tipo = random.randint(1,3)
        tipo_nave = mandale_nave(tipo)
        #(self,posx,posy,puntaje,nivel,parametro,tipo="Minion",cantVidas=1) -> None:
        lista_enemigos.append(Enemigos(i*TAMANIO_NAVE_ENEMIGA,j*TAMANIO_NAVE_ENEMIGA,10,1,tipo_nave,"Minion",tipo))

#CREAMOS BOSS
tipo_nave = mandale_boss(random.randint(1,2))
boss = Enemigos(int(ANCHO_VENTANA/2),100,10,1,tipo_nave,"Boss",20)

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",TAM_SCORE)

imagen_fondo = pygame.image.load(PATH_IMG+"fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#Sonido del juego
pygame.mixer.music.load("music/stage1.mp3")
volumen = 0.1
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

#Sentido de las naves enemigas
sentido = "DER"
final_boss = True
entro = True
iniciar_intro = False
nivel = 1
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
    aumentar_limite_disparos = 0
    puntuacion = 0
    for nave in lista_enemigos:
        # puntuacion+=nave.puntaje
        if(nave.mostrar):
            nave.update(delta_ms,potenciador,player.disparos)
            nave.draw(ventana_principal)
            #Aumentamos los disparos si bajan los enemigos
            nave.limite_disparos+=(len(lista_enemigos)-total_enemigos_vivos)
        else:
            puntuacion += nave.puntaje
        for misil in nave.disparos: 
            if not player.inmune:
                if misil.rectangulo.colliderect(player.rectangulo):
                    player.control("DEAD")
                    misil.mostrar = False
            misil.actualizar_pantalla(ventana_principal,nave.velocidad_disparo,"Minion")

    if(total_enemigos_vivos==0 and final_boss):
        
        #Preparamos la intro para el boss
        if(entro):
            tiempo=0
        tiempo+=delta_ms
        entro = False
        volumen = 500/tiempo
        pygame.mixer.music.set_volume(volumen)
        if volumen < 0.1:
            pygame.mixer.music.play()
            pygame.mixer.music.load("music/finalBoss.mp3")
            pygame.mixer.music.play(-1)
            final_boss = False
    
    if iniciar_intro:
        boss.intro_boss(delta_ms)
    
    if (not final_boss):
        pygame.mixer.music.set_volume(0.5)
        boss.update(delta_ms,potenciador,player.disparos)
        boss.draw(ventana_principal)
        iniciar_intro = True

        for misil in boss.disparos: 
            if not player.inmune:
                if misil.rectangulo.colliderect(player.rectangulo):
                    player.control("DEAD")
                    misil.mostrar = False
            misil.actualizar_pantalla(ventana_principal,boss.velocidad_disparo,"Boss")
    texto_score = fuente.render("{}: {}".format("score: ",puntuacion), True, colores.COLOR_AMARILLO_ARENA)
    texto_nivel = fuente.render("{}: {}".format("nivel: ",nivel), True, colores.COLOR_AMARILLO_ARENA)
    ventana_principal.blit(texto_score, (ANCHO_VENTANA*0.8,0))
    ventana_principal.blit(texto_nivel, (ANCHO_VENTANA*0.1,0))
    posvidas = (ANCHO_VENTANA,ALTO_VENTANA)
    for elem in range(player.vidas):
        vida = pygame.image.load(PATH_IMG+"ship.png")
        vida = pygame.transform.scale(vida,TAM_VIDAS)    
        ventana_principal.blit(vida, (elem*vida.get_width(),ALTO_VENTANA-vida.get_height() - 5))

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()