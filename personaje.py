import pygame
import colores
from helpers import *
from constantes import *
from disparos import Disparar



class NavePpal:
    def __init__(self,posx,posy) -> None:
            self.quieto = get_superficie_sprite(PATH_IMG+"player_ship.png",4,1)
            self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
            self.muere = escalar(self.muere)
            self.frame = 0
            self.animacion = self.quieto
            self.imagen = self.animacion[self.frame]
            self.animacion_repetir = True
            self.tiempo = 0
            self.tiempo_inmune = 0
            self.limite_disparos = 5
            self.velocidad = 5
            self.vidas = 3
            self.score = 0
            # self.superficie =  pygame.transform.scale(pygame.image.load(path),(ancho,alto))
            self.mostar = True
            self.disparos = []
            self.velocidad_disparo = 5
            self.inmune = False

            self.rectangulo = self.imagen.get_rect()
            self.rectangulo.centerx = posx
            self.rectangulo.y = posy
    
    def shot(self):
        if(self.limite_disparos > len(self.disparos)):
            disparo = Disparar(self.rectangulo.centerx,self.rectangulo.y)
            self.disparos.append(disparo)

    def movimiento(self,tiempo):
        if self.tiempo > 100:
            self.tiempo = 0
            if(self.frame < len(self.animacion)-1):
                self.frame +=1
            else:
                if(self.animacion_repetir):
                    self.frame = 0
                else:
                    self.mostar = False
        else:
            self.tiempo+=tiempo

    def disparar(self):
        if(len(self.disparos) > 0):
            if(self.disparos[0].rectangulo.y < 0 or not(self.disparos[0].mostrar)):
                self.disparos.pop(0)

    def update(self,tiempo):

        self.disparar()

        if(self.mostar):
            self.movimiento(tiempo)

        if(self.inmune):
            self.tiempo_inmune+=tiempo
            if(self.tiempo_inmune > 1000):
                self.limite_disparos = 5
                self.inmune = False
                self.tiempo_inmune=0

        if(self.animacion == self.muere):
            self.tiempo += tiempo
            if(self.tiempo > 1000):
                self.vidas -=1
                if(self.vidas > 0):
                    self.frame = 0
                    self.tiempo = 0
                    self.animacion = self.quieto
                    self.mostar = True
                    self.animacion_repetir = True
                    self.inmune = True
                    self.rectangulo.centerx=int(ANCHO_VENTANA/2)
                else:
                    #GAME OVER
                    pass
            # self.limite_disparos=0

    def draw(self,pantalla):
        # pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, self.rectangulo)
        if(self.mostar):
            self.imagen = self.animacion[self.frame]
            pantalla.blit(self.imagen, self.rectangulo)

    def control(self, accion):
        ancho_nave = self.rectangulo.width
        if(accion == "STAY"):
            lista_teclas = pygame.key.get_pressed()
            if lista_teclas[pygame.K_RIGHT] and self.rectangulo.x < ANCHO_VENTANA - ancho_nave:
                self.rectangulo.x = self.rectangulo.x + self.velocidad
            if lista_teclas[pygame.K_LEFT] and self.rectangulo.x > 0:
                self.rectangulo.x = self.rectangulo.x - self.velocidad
        if(accion == "SHOT"):
            self.shot()
        if(accion == "DEAD"):
            self.animacion = self.muere
            self.limite_disparos = 0
            self.animacion_repetir = False
           
