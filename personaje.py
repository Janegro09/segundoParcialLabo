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
            
            self.disparar_animacion = []
            self.quieto = get_superficie_sprite(PATH_IMG+"player_ship.png",4,1)
            self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",2,3)
            self.frame = 1

            self.animacion = self.quieto
            self.imagen = self.animacion[self.frame]
            self.rectangulo = self.imagen.get_rect()
            self.rectangulo.centerx = posx
            self.rectangulo.y = posy


    def update(self, pantalla):
        if(self.frame < len(self.animacion)-1):
             self.frame +=1
        else:
             self.frame = 0
    
    def draw(self,pantalla):
        # pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, self.rectangulo)

        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen, self.rectangulo)
         

    def mover(self,ancho,alto):
        ancho_nave = self.rectangulo.width
        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_RIGHT] and self.rectangulo.x < ancho - ancho_nave:
            self.rectangulo.x = self.rectangulo.x + self.velocidad
        if lista_teclas[pygame.K_LEFT] and self.rectangulo.x > 0:
            self.rectangulo.x = self.rectangulo.x - self.velocidad
