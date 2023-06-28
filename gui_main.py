import pygame
import colores
import random
from helpers import *
from enemigos import Enemigos
from personaje import NavePpal
from constantes import *
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC

pygame.init()
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GALAGA")

form_menu = FormMenuA(name="form_menu",master_surface=ventana_principal,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_back=colores.COLOR_NEGRO, color_border=colores.COLOR_AMARILLO_MOSTAZA,active=True)

form_menu2 = FormMenuB(name="form_menu2",master_surface=ventana_principal,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_back=colores.COLOR_NEGRO, color_border=colores.COLOR_AMARILLO_MOSTAZA,active=False)

form_menu_game_over = FormMenuC(name="form_menu_game_over",master_surface=ventana_principal,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_back=colores.COLOR_NEGRO, color_border=colores.COLOR_AMARILLO_MOSTAZA,active=False)

flag_run = True

# TIMER fabrique un evento independiente del usuario que se ejecuta una vez cada mls que le indique
timer = pygame.USEREVENT
pygame.time.set_timer(timer,100)
flag_limite = True
clock = pygame.time.Clock()
#Creamos personaje ppal
player = NavePpal(ANCHO_VENTANA/2,ALTO_VENTANA-100)

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",TAM_SCORE)

imagen_fondo = pygame.image.load(PATH_IMG+"fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#Sentido de las naves enemigas
sentido = "DER"
nivel = 1
nivel_actual=1
puntuacion = 0
lvl_final =False
while flag_run:
    
    if(nivel == nivel_actual and nivel_actual<=5):
        #CREAMOS ENEMIGOS
            
        entro = True
        final_boss = True
        iniciar_intro = False
        nivel_actual+=1
        tipo_nave = mandale_boss(random.randint(1,2))
        if(nivel_actual==6):
            entro = False
            final_boss = False
            iniciar_intro = True
            tipo_nave = NAVE_BOSS_3
        #CREAMOS BOSS
        boss = Enemigos(int(ANCHO_VENTANA/2),100,10,nivel,tipo_nave,"Boss",20)

        total_filas = range(obtener_filas(nivel))
        total_columnas = range(obtener_columnas(nivel))

        lista_enemigos = []

        for i in total_columnas:
            for j in total_filas:
                tipo = random.randint(1,3)
                tipo_nave = mandale_nave(tipo)
                #(self,posx,posy,puntaje,nivel,parametro,tipo="Minion",cantVidas=1) -> None:
                lista_enemigos.append(Enemigos(i*TAMANIO_NAVE_ENEMIGA,j*TAMANIO_NAVE_ENEMIGA,10,nivel,tipo_nave,"Minion",tipo))


        #Sonido del juego
        pygame.mixer.music.load("music/stage1.mp3")
        volumen = 1

        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1)



    ventana_principal.blit(imagen_fondo,imagen_fondo.get_rect())
    # ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)
    delta_ms = clock.tick(FPS)
    
    #PLAYER UPDATE
    player.control("STAY")

    lista_eventos = pygame.event.get()
    # ENEMY DRAW&UPDATE
    total_enemigos_vivos = contar_enemigos_vivos(lista_enemigos)
    for evento in lista_eventos:
        if (evento.type == pygame.QUIT):
            flag_run = False

        if evento.type == pygame.KEYDOWN:
            if(evento.key == pygame.K_SPACE):
                player.control("SHOT")

        if evento.type == pygame.USEREVENT:
            #Corto antes de que la lista de mover naves para mostrar sean vacias
            sentido = mover_naves(lista_enemigos, sentido)
            # if(len(lista_enemigos) - total_enemigos_vivos) !=len(lista_enemigos) :

    # PERSONAJE DRAW&UPDATE
    player.update(delta_ms)
    player.draw(ventana_principal)
    # SHOT DRAW
    for misil in player.disparos:
        misil.actualizar_pantalla(ventana_principal,player.velocidad)

    potenciador = 1 if total_enemigos_vivos==0 else int(len(lista_enemigos)/total_enemigos_vivos)
    aumentar_limite_disparos = 0

    for nave in lista_enemigos:
        # puntuacion+=nave.puntaje
        if(nave.mostrar):
            nave.update(delta_ms,potenciador,player.disparos)
            nave.draw(ventana_principal)
            #Aumentamos los disparos si bajan los enemigos
            nave.limite_disparos+=(len(lista_enemigos)-total_enemigos_vivos)
        else:
            puntuacion += nave.puntaje
            nave.puntaje = 0
        for misil in nave.disparos: 
            if not player.inmune:
                if misil.rectangulo.colliderect(player.rectangulo):
                    player.control("DEAD")
                    misil.mostrar = False
            misil.actualizar_pantalla(ventana_principal,nave.velocidad_disparo,"Minion")

    if((total_enemigos_vivos==0 and final_boss) or lvl_final):
        
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
        if(not boss.mostrar):
            nivel+=1
            print("se murió")
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
    
    if(form_menu.active):
        form_menu.update(lista_eventos)
        form_menu.draw()

    if(form_menu2.active):
        form_menu2.update(lista_eventos)
        form_menu2.draw()

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()