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
player = personaje.crear(ANCHO_VENTANA/2, ALTO_VENTANA - 80,36,36,"img\ship.png")
#CREAMOS ENEMIGOS
lista_enemigos1 = enemigos.crear_lista_enemigos(6,0,0,60,60,"img\spiked1.PNG")
lista_enemigos2 = enemigos.crear_lista_enemigos(6,0,70,60,60,"img\spiked2.PNG")
lista_enemigos3 = enemigos.crear_lista_enemigos(6,0,140,60,60,"img\spiked3.PNG")

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
                    sentido = enemigos.update_right(lista_enemigos1,ANCHO_VENTANA,30,sentido)
                    sentido = enemigos.update_right(lista_enemigos2,ANCHO_VENTANA,30,sentido)
                    sentido = enemigos.update_right(lista_enemigos3,ANCHO_VENTANA,30,sentido)
                else:
                    sentido = enemigos.update_left(lista_enemigos1,ANCHO_VENTANA,30,sentido)
                    sentido = enemigos.update_left(lista_enemigos2,ANCHO_VENTANA,30,sentido)
                    sentido = enemigos.update_left(lista_enemigos3,ANCHO_VENTANA,30,sentido)

        personaje.mover(player, ANCHO_VENTANA, ALTO_VENTANA)


    ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)

    personaje.actualizar_pantalla(player, ventana_principal)
    enemigos.actualizar_pantalla(lista_enemigos1,ventana_principal)
    enemigos.actualizar_pantalla(lista_enemigos2,ventana_principal)
    enemigos.actualizar_pantalla(lista_enemigos3,ventana_principal)
    
    pygame.display.flip()

pygame.quit()