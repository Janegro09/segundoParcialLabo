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
        # print(i*TAMANIO_NAVE_ENEMIGA,j*TAMANIO_NAVE_ENEMIGA)
        # self,posx,posy,puntaje,nivel,parametro,tipo="Minion",cantVidas=1
        lista_enemigos.append(Enemigos(i*TAMANIO_NAVE_ENEMIGA,j*TAMANIO_NAVE_ENEMIGA,10,1,tipo_nave,"Minion",tipo))

#CREAMOS BOSS
tipo_nave = mandale_boss(random.randint(1,2))
boss = Enemigos(int(ANCHO_VENTANA/2),0,10,1,tipo_nave,"Boss",1)


#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",20)
texto = fuente.render("PUNTAJE:", True, colores.COLOR_AMARILLO_ARENA)

imagen_fondo = pygame.image.load(PATH_IMG+"fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#Sonido del juego
pygame.mixer.music.load("music/stage1.mp3")
volumen = 1
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

#Sentido de las naves enemigas
sentido = "DER"
final_boss = True
entro = True
iniciar_intro = False
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
    for nave in lista_enemigos:
        if(nave.mostrar):
            nave.update(delta_ms,potenciador,player.disparos)
            nave.draw(ventana_principal)
            #Aumentamos los disparos si bajan los enemigos
            nave.limite_disparos+=(len(lista_enemigos)-total_enemigos_vivos)

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
            misil.actualizar_pantalla(ventana_principal,nave.velocidad_disparo,"Boss")

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()