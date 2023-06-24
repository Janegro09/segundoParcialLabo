import pygame
from constantes import *

class Disparar:
    def __init__(self,posx,posy, tipo="normal") -> None:
        self.mostrar = True
        self.surface_image = pygame.image.load(PATH_IMG+"laser.png")
        if tipo == "Minion":
            self.surface_image = pygame.transform.rotate(pygame.image.load(PATH_IMG+"laserRed.png"), 180)
        if tipo == "Boss":
            self.surface_image = pygame.transform.rotate(pygame.image.load(PATH_IMG+"laserRedBoss.png"), 180)
        self.rectangulo = self.surface_image.get_rect()
        self.rectangulo.x = posx-3
        self.rectangulo.y = posy-3
        self.mostrar = True

    def mover(self,velocidad,tipo="normal"):
        if(tipo=="Minion" or tipo=="Boss"):
            self.rectangulo.y +=velocidad
        else:
            self.rectangulo.y -=velocidad

    def actualizar_pantalla(self,pantalla,velocidad,tipo="normal"):
        self.mover(velocidad,tipo)
        # pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, self.rectangulo)
        if self.mostrar:
            pantalla.blit(self.surface_image, self.rectangulo)