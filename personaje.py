import pygame
import colores
from helpers import *
from constantes import *



class NavePpal:
    def __init__(self,posx,posy) -> None:
            self.velocidad = 5
            self.vidas = 3
            self.score = 0
            
            # self.superficie =  pygame.transform.scale(pygame.image.load(path),(ancho,alto))
            self.mostar = True
            self.disparar_animacion = []
            self.quieto = get_superficie_sprite(PATH_IMG+"player_ship.png",4,1)
            self.quieto = get_superficie_sprite(PATH_IMG+"player_ship.png",4,1)
            self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
            self.muere = escalar(self.muere)
            self.animacion_repetir = True
            self.frame = 0

            self.animacion = self.quieto
            self.imagen = self.animacion[self.frame]
            self.rectangulo = self.imagen.get_rect()
            self.rectangulo.centerx = posx
            self.rectangulo.y = posy


    def update(self):
        
        if(self.frame < len(self.animacion)-1):
             self.frame +=1
        else:
            if(self.animacion_repetir):
                self.frame = 0
            else:
                self.mostar = False

    
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
             self.animacion = self.muere
             self.animacion_repetir = False
