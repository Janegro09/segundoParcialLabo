import pygame
from constantes import *

class Disparar:
    def __init__(self,posx,posy) -> None:
        self.mostrar = True
        self.surface_image = pygame.image.load(PATH_IMG+"laser.png")
        self.rectangulo = self.surface_image.get_rect()
        self.rectangulo.x = posx-3
        self.rectangulo.y = posy-3
        self.choco = False
        
    def mover(self):
        self.rectangulo.y -=DESPLAZAMIENTO

    def actualizar_pantalla(self,pantalla):
        self.mover()
        # pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, self.rectangulo)
        pantalla.blit(self.surface_image, self.rectangulo)