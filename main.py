import pygame
import colores
import enemigos
import personaje


ALTO_VENTANA = 600
ANCHO_VENTANA = 720

# pos_circulo = [0-80,60]
# pos_circulo2 = [ANCHO_VENTANA-80*1.25,60]
# pos_circulo = [0-80,60]
# pos_circulo2 = [0-80*1.5,60]

pygame.init()
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GALAGA")

flag_run = True

# TIMER fabrique un evento independiente del usuario que se ejecuta una vez cada mls que le indique
timer = pygame.USEREVENT
pygame.time.set_timer(timer,500)
# timer_segundo2 = pygame.USEREVENT
# pygame.time.set_timer(timer_segundo2,10)
flag_limite = True
# flag_limite2 = True

#Creamos personaje ppal
player = personaje.crear(ANCHO_VENTANA/2, ALTO_VENTANA - 80,36,36)
#CREAMOS ENEMIGOS
lista_enemigos = enemigos.crear_lista_enemigos(6)

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",20)
texto = fuente.render("PUNTAJE:", True, colores.COLOR_AMARILLO_ARENA)
sentido = True

while flag_run:

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if (evento.type == pygame.QUIT):
            flag_run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            rec_pos = evento.pos
        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                if(sentido):
                    sentido = enemigos.update_right(lista_enemigos,ANCHO_VENTANA,30,sentido)
                else:
                    sentido = enemigos.update_left(lista_enemigos,ANCHO_VENTANA,30,sentido)

        lista_teclas = pygame.key.get_pressed()
        # if lista_teclas[pygame.K_RIGHT] and rec_pos[0] < ANCHO_VENTANA - REC_TAM[0]:
        #     rect_nave[0] = rect_nave[0] + 5

        # if lista_teclas[pygame.K_LEFT] and rec_pos[0] > 0:
        #     rect_nave[0] = rect_nave[0] - 5
        # if lista_teclas[pygame.K_UP] and rec_pos[1] > 0:
        #     rec_pos[1] = rec_pos[1] - 5
        # if lista_teclas[pygame.K_DOWN] and rec_pos[1] < ALTO_VENTANA - REC_TAM[1]:
        #     rec_pos[1] = rec_pos[1] + 5


    ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)

    personaje.actualizar_pantalla(player, ventana_principal)
    enemigos.actualizar_pantalla(lista_enemigos,ventana_principal)
    
    pygame.display.flip()

pygame.quit()