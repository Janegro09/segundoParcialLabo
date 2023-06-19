import pygame
import colores

class NavePpal:
    def __init__(self,path,ancho,alto,x,y) -> None:
            
            self.superficie =  pygame.transform.scale(pygame.image.load(path),(ancho,alto))
            self.rectangulo = self.superficie.get_rect()
            self.rectangulo.centerx = x
            self.rectangulo.y = y
    
    def actualizar_pantalla(self,pantalla):
        pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, self.rectangulo)
        pantalla.blit(self.superficie, self.rectangulo)
         

    def mover(self,ancho,alto):
        ancho_nave = self.rectangulo.width
        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_RIGHT] and self.rectangulo.x < ancho - ancho_nave:
            self.rectangulo.x = self.rectangulo.x + 1
        if lista_teclas[pygame.K_LEFT] and self.rectangulo.x > 0:
            self.rectangulo.x = self.rectangulo.x - 1
        # if lista_teclas[pygame.K_UP] and nave[1] > 0:
        #     nave[1] = nave[1] - 5
        # if lista_teclas[pygame.K_DOWN] and nave[1] < alto - ancho_nave:
        #     nave[1] = nave[1] + 5