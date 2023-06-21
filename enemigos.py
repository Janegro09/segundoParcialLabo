import pygame
import colores
from constantes import *
from helpers import *

class NaveVerde:
    def __init__(self,posx,posy,ancho,alto,puntaje,parametro) -> None:

        self.superficie = get_superficie_sprite(PATH_IMG+parametro,1,1)
        self.superficie = escalar(self.superficie,(TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA))
        self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
        self.muere = escalar(self.muere)
        self.frame = 0
        self.animacion = self.superficie
        self.imagen = self.animacion[self.frame]
        self.animacion_repetir = True

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posx
        self.rectangulo.y = posy
        
        self.mostrar = True
        self.puntaje = puntaje

    def mover_derecha(self):
        self.rectangulo.x +=DESPLAZAMIENTO

    def mover_izquierda(self):
        self.rectangulo.x -=DESPLAZAMIENTO

    def mover(self, direccion):
        if(direccion):
            self.mover_derecha()
        else:
            self.mover_izquierda()

    def update(self, disparos=[]):

        for misil in disparos:
            if self.rectangulo.colliderect(misil.rectangulo):
                self.animacion = self.muere
        if(self.animacion == self.muere):
            if(self.frame < len(self.animacion)-1):
                self.frame +=1
            else:
                self.mostrar = False

        self.imagen = self.animacion[self.frame]

    def draw(self,pantalla):
        if(self.mostrar):
            pantalla.blit(self.imagen, self.rectangulo)

    @property
    def posicion(self):
        return self.rectangulo.x


def update(lista_enemigos, ancho, tam, nave_ppal, sentido = True):
    if(sentido):
        sentido = update_right(lista_enemigos,ancho,30,sentido, nave_ppal)
        # sentido = enemigos.update_right(lista_enemigos2,ANCHO_VENTANA,30,sentido)
        # sentido = enemigos.update_right(lista_enemigos3,ANCHO_VENTANA,30,sentido)
    else:
        sentido = update_left(lista_enemigos,ancho,30,sentido, nave_ppal)
        # sentido = enemigos.update_left(lista_enemigos2,ANCHO_VENTANA,30,sentido)
        # sentido = enemigos.update_left(lista_enemigos3,ANCHO_VENTANA,30,sentido)

def update_left(lista_enemigos, ancho, tam, cambiar_sentido, nave_ppal):
    primera_nave = lista_enemigos[0]
    #muevo a la izquierda
    if(primera_nave["rect"][0] > 0  ):
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[0] = rect_enemigo[0] - 10
            if rect_enemigo.colliderect(nave_ppal["rect"]):
                print("Choco")
    #bajo todo
    else:
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[1] = rect_enemigo[1] + tam
        cambiar_sentido = not(cambiar_sentido)
        print(primera_nave["rect"][0])

    return cambiar_sentido

def update_right(lista_enemigos, ancho, tam, cambiar_sentido, nave_ppal):
    ultima_nave = lista_enemigos[len(lista_enemigos) - 1]
    #muevo a la derecha
    ancho_nave = ultima_nave["rect"].width
    if(ultima_nave["rect"][0] < ancho - ancho_nave ):
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[0] = rect_enemigo[0] + 10
            if rect_enemigo.colliderect(nave_ppal["rect"]):
                print("Choco")

    #bajo todo
    else:
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[1] = rect_enemigo[1] + tam
        cambiar_sentido = not(cambiar_sentido)
        print(ultima_nave["rect"][0])

    return cambiar_sentido



# def crear_lista_enemigos(cant, x, y, ancho, alto, path_imagen):
#     lista_naves = []
#     pos_naves = 0
#     for i in range(cant):
#         lista_naves.append(crear_enemigo(x+pos_naves,y,ancho, alto, path_imagen))
#         pos_naves=ancho + pos_naves +10
#     return lista_naves