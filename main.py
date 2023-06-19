import pygame
import colores
from enemigos import NaveVerde
from personaje import NavePpal

ALTO_VENTANA = 600
ANCHO_VENTANA = 720

pygame.init()
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GALAGA")

flag_run = True

# TIMER fabrique un evento independiente del usuario que se ejecuta una vez cada mls que le indique
timer = pygame.USEREVENT
pygame.time.set_timer(timer,100)
flag_limite = True

#Creamos personaje ppal
player = NavePpal("img\ship.png",36, 36,ANCHO_VENTANA/2,ALTO_VENTANA - 80)

#CREAMOS ENEMIGOS
total_enemigos = range(5)
lista_enemigos_verde = []
for i in total_enemigos:
    lista_enemigos_verde.append(NaveVerde(0+i*70,0,60,60,10,"img\spiked2.PNG"))

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
            for nave in lista_enemigos_verde: 
                nave.mover()

    player.mover(ANCHO_VENTANA, ALTO_VENTANA)

    ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)

    player.actualizar_pantalla(ventana_principal)
    for nave in lista_enemigos_verde:
        nave.actualizar_pantalla(ventana_principal)

    pygame.display.flip()

pygame.quit()